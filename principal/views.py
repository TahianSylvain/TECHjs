import datetime
# from django.utils.datetime_safe import strftime

from .models import Annotation
from .forms import AnnotationForm
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, reverse
from django.shortcuts import render, get_object_or_404, get_list_or_404

import openai
from openai.error import APIConnectionError


def chatbot_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0]["text"]


def visiting(request, user_id):
    utilisateur = get_object_or_404(User, pk=user_id)
    ses_annotations = get_list_or_404(Annotation, account=utilisateur)
    return render(
        request,
        template_name='principal/userProfile.html',
        context={'u': utilisateur, 'annotate': ses_annotations},
        status=200
    )


def principal(request, annotation_id=0):
    if request.user.username:
        nature: str = "Add"
        advice: str = "Getting connection to openai..."
        length: float = 0
        timing: str = ''
        qs = Annotation.objects.filter(account=request.user).order_by("deadline")
        if request.method == 'POST':
            if annotation_id == 0:
                desc = request.POST['description']
                form = Annotation.objects.create(
                    account=request.user, over=False, name=request.POST['name'],
                    deadline=request.POST['deadline'],
                    reminder=request.POST['reminder'], description=desc
                )  # create
                form.save()
                return HttpResponseRedirect(reverse('main:entry'))
            else:
                nature = 'change'
                note = Annotation.objects.get(id=annotation_id)
                form = AnnotationForm(request.POST, instance=note)
                if form.is_valid():
                    form.save()
                return render(request, template_name='principal/main.html', context={"dj": qs, "form": form, "type": nature})
        elif request.method == 'GET':
            if annotation_id == 0:
                form = AnnotationForm()  # create
            else:
                nature = 'change'
                note = Annotation.objects.get(id=annotation_id)
                try:
                    advice = chatbot_response(  # string regular expression
                        'I have a task named ' + note.name + r', that is described as this: ' + note.description +
                        r'. Can You help me to make it well done as quick as possible?'
                    )
                except APIConnectionError:
                    response = 'Oh! It seems that connection has temporarily stopped!'
                coming_deadline = note.deadline
                delta = datetime.datetime(year=coming_deadline.year, month=coming_deadline.month,
                                          day=coming_deadline.day, hour=coming_deadline.hour,
                                          minute=coming_deadline.minute, second=coming_deadline.second, microsecond=0)
                if delta > datetime.datetime.now():
                    timing = 'blue'  # restful
                    final = delta - datetime.datetime.now()
                else:
                    timing = 'red'  # late
                    final = datetime.datetime.now() - delta
                # 100% === 300px === 0s  // 0% === Opx === n_seconds  |
                length = abs(round(100 * 3 / (1+(final.total_seconds()/1000))))
                print('now it\'s', end=f'{datetime.datetime.now()}\n')
                form = AnnotationForm(instance=note)
            return render(
                    request,
                    template_name='principal/main.html',
                    context={
                        "dj": qs,
                        "form": form,
                        "type": nature,
                        "advice": advice,
                        "length": length,
                        "timing": timing,
                    }
                )

    elif request.user:  # new_User_or_Anonymous
        qs = User.objects.all()  # async filter(is_active=True, good_stat)

        """ matplotlib(user, login) """

        return render(request, template_name='./principal/main.html', context={"dj": qs})


def delete(request, annotation_id):
    notif = Annotation.objects.get(id=annotation_id)
    if notif.account == request.user:  # only owner can delete his/her object
        notif.delete()
    return HttpResponseRedirect(reverse("main:entry"))

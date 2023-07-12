import datetime
from asgiref.sync import sync_to_async
from django.http import JsonResponse

from .models import Annotation
from .forms import AnnotationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from django.shortcuts import HttpResponseRedirect, reverse
from django.shortcuts import render, get_object_or_404, get_list_or_404

import openai
from openai.error import APIConnectionError


@sync_to_async()
@login_required(login_url='account:login')
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


@sync_to_async()
def visiting(request, user_id):
    """ u = User.objects.all()"""
    utilisateur = get_object_or_404(User, pk=user_id)

    # print(utilisateur.id)
    ses_annotations = get_list_or_404(Annotation, account=utilisateur)
    return render(
        request,
        template_name='principal/userProfile.html',
        context={'u': utilisateur, 'annotate': ses_annotations},
        status=200
    )


@sync_to_async()
@login_required(login_url='account:login')
def search_results(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest': # request.is_ajax():
        annotation = request.POST['annotation']
        
        qs = Annotation.objects.filter(name__icontains=annotation)
        print(qs)
        if (len(qs)>0) and (len(annotation)>0):
            data = []
            for pos in qs:
                item = {
                    "pk": pos.pk,
                    "name": pos.name,
                    "account": pos.account,
                    # "deadline", "reminder", "description"
                }
                data.append(item)
            res = data
        else:
            res = 'No annotation found'
        return JsonResponse({'data': res})
    JsonResponse({})


@sync_to_async()
def generated(request, annotation_id=0):
    if request.user.username:
        nature: str = "Add"
        advice: str = "Getting connection to openai..."
        length: float = 0
        timing: str = ''
        qs = Annotation.objects.filter(account=request.user).order_by("deadline")
        for note in qs:
            coming_deadline = note.deadline
            delta = datetime.datetime(year=coming_deadline.year, month=coming_deadline.month,
                                      day=coming_deadline.day, hour=coming_deadline.hour,
                                      minute=coming_deadline.minute, second=coming_deadline.second, microsecond=0)
            if (delta - datetime.datetime.now()).total_seconds() < 0 and note.over is False:
                print(note)
                note.over = True
            elif (delta - datetime.datetime.now()).total_seconds() > 0 and note.over:
                note.over = False
            note.save()
        if request.method == 'POST':
            if annotation_id == 0:
                desc = request.POST['description']
                form = Annotation.objects.create(
                    account=request.user,
                    name=request.POST['name'],
                    deadline=request.POST['deadline'],
                    reminder=request.POST['reminder'], description=desc,
                    over=False
                )  # create
                deadline = datetime.datetime(year=int(request.POST['deadline'][0:3]),
                                             month=int(request.POST['deadline'][5:7]),
                                             day=int(request.POST['deadline'][8:10]),
                                             hour=int(request.POST['deadline'][11:13]),
                                             minute=int(request.POST['deadline'][14:16]),
                                             second=10, microsecond=10)
                if (deadline - datetime.datetime.now()).total_seconds() > 0:
                    over = False  # temps impartie finie
                else:
                    over = True

                form.over = over
                form.save()
                return HttpResponseRedirect(reverse('main:entry'))
            else:
                nature = 'change'
                note = Annotation.objects.get(id=annotation_id)
                form = AnnotationForm(request.POST, instance=note)
                if form.is_valid():
                    form.save()
                return HttpResponseRedirect(reverse('main:entry'))

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
                length = abs(round(100 * 3 / (1 + (final.total_seconds() / 1000))))
                '''print('now it\'s', end=f'{datetime.datetime.now()}\n')'''
                form = AnnotationForm(instance=note)
            return render(request, template_name='principal/generat.html', context={  # 'principal/timer.html'
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

        return render(request, template_name='./principal/generat.html', context={"dj": qs})


@sync_to_async
@login_required(login_url='account:login')
def listing_tasks_by_time(request, annotate_deadline_date):  # '%Y-%m-%d %H:%M:%S'
    """ http://localhost:3333/journey/on2023-05-19 18:32:24/ """
    annee = int(annotate_deadline_date[0:4])
    mois = str(annotate_deadline_date[5:7])
    if '-' in mois:
        mois = int(annotate_deadline_date[5])
    jour = str(annotate_deadline_date[7:10])
    print(jour)
    if '-' in jour:
        jour.replace('-', '')
    on_this_day = datetime.date(year=int(annee),
                                month=int(mois),
                                day=int(jour))
    qs = Annotation.objects.filter(over=True)
    right_qs = [item for item in qs if on_this_day == item.deadline.date()]
    return render(request, './principal/main.html', context={'dj': right_qs}, status=200)


@sync_to_async()
@login_required(login_url="account:login")
def delete(request, annotation_id):
    notif = Annotation.objects.get(id=annotation_id)
    if notif.account == request.user:  # only owner can delete his/her object
        notif.delete()
    return HttpResponseRedirect(reverse("main:entry"))

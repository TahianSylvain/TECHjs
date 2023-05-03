import datetime

from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, reverse
from .forms import AnnotationForm
from .models import Annotation


def principal(request, annotation_id=0):
    if request.user.username:
        nature: str = "Add"
        length: float = 0
        timing: str = ''
        qs = Annotation.objects.filter(account=request.user).order_by("deadline")

        if request.method == 'POST':
            if annotation_id == 0:
                form = AnnotationForm(request.POST)  # create
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
            return render(request, template_name='principal/main.html', context={"length": length, "timing": timing,
                                                                                 "dj": qs, "form": form, "type": nature})

    elif request.user:  # new_User_or_Anonymous
        qs = User.objects.all()
        return render(request, template_name='./frontend/public/index.html', context={"dj": qs})


def delete(request, annotation_id):
    notif = Annotation.objects.get(id=annotation_id)
    if notif.account == request.user:  # only owner can delete his/her object
        notif.delete()
    return HttpResponseRedirect(reverse("main:entry"))

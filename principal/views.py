from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, reverse
from .forms import AnnotationForm
from .models import Annotation


def principal(request, annotation_id=0):
    if request.user.username:
        nature: str = "Add"
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
                form = AnnotationForm(instance=note)
            return render(request, template_name='principal/main.html', context={"dj": qs, "form": form, "type": nature})

    elif request.user:  # new_User_or_Anonymous
        qs = User.objects.all()
        return render(request, template_name='principal/main.html', context={"dj": qs})


def delete(request, annotation_id):
    notif = Annotation.objects.get(id=annotation_id)
    notif.delete()
    return HttpResponseRedirect(reverse("main:entry"))

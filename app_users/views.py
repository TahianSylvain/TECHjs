from asgiref.sync import sync_to_async
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from app_users.forms import SignUpUserForm


# Django Axes
@sync_to_async()
def register(request):
    if request.method == 'POST':
        user_form = SignUpUserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.save()
            login(request, user)
        else:
            print(user_form.errors)
    else:
        user_form = SignUpUserForm()

    return render(request, 'app_users/sign_up.html', context={
        'user_form': user_form,
    })


# Django Axes
@sync_to_async()
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main:entry'))
            else:
                return HttpResponse('Account is deactivated!')
        else:
            return HttpResponse('Please, Use correct name or password!')
    else:
        return render(request, 'app_users/log_in.html')


@login_required(login_url='account:login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:entry'))


@login_required(login_url='account:login')
def switch_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:login'))

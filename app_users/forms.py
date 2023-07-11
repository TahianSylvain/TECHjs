from django import forms
from django.contrib.auth.models import User
from app_users.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm


class SignUpUserForm(UserCreationForm):
    username = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={'id': "username"}
        )
    )
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(
            attrs={'id': "username"}
        )
    )
    password1 = forms.CharField(
        required=True, widget=forms.PasswordInput(
            attrs={'id': "password"}
        )
    )
    password2 = forms.CharField(
        required=True, widget=forms.PasswordInput(
            attrs={'id': "password"}
        )
    )

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2')
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }


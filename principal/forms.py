from django import forms
from .models import Annotation


class AnnotationForm(forms.ModelForm):
    name = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={
                'class': "form-input", 'id': "firstname",
                'placeholder': "enter the title's"
            }
        )
    )
    description = forms.CharField(
        required=True, widget=forms.Textarea(
            attrs={
                'class': "form-input", 'id': "choose-file",
                'placeholder': "describe all steps you need to achieve",
                'rows': "4", 'cols': "50", 'style': "height:auto"
            }
        )
    )
    reminder = forms.TimeField(
        required=True, widget=forms.TimeInput(
            attrs={
                "type": "time",
                'id': "timing",
            }
        )
    )
    deadline = forms.DateTimeField(
        required=True, widget=forms.DateTimeInput(
            attrs={
                'type': "datetime-local",
                'id': "lastname",
                'class': "form-input",
                "placeholder": "enter the time over"
            }
        )
    )

    class Meta:
        model = Annotation
        fields = ['name', 'description', 'deadline', 'reminder']

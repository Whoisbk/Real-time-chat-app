from django import forms
from django.contrib.auth.models import User


class SigninUser(forms.Form):
    username = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'class':'username',
        'title':'name',
        }))
    pass1 = forms.CharField(required=False,max_length=32,label="",widget=forms.PasswordInput(
        attrs={'class':'password-input',
        }))


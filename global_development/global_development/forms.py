from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username', 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'form-control', 'placeholder': 'Password', 'required': True}))

    class Meta:
        model = User
        fields = ('username', 'password')
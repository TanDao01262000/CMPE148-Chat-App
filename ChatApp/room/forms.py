from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms


class UserRegisterForm(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OpenNewRoom(forms.Form):
    room_name = forms.CharField(max_length=255)
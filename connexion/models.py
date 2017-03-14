from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class AuthentificationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import AuthentificationForm
from django.forms import ModelForm


def connexion(request):
	form = AuthentificationForm()
	return render(request, 'registration/login.html', {'form':form})
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from .models import AuthentificationForm
from django.forms import ModelForm


def connexion(request):
	form = AuthentificationForm()
	return render(request, 'registration/login.html', {'form':form})

def deconnexion(request):
	logout(request, next_page='/')
	return render(request, '/')
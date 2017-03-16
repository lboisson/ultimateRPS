from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

from game.models import Game



def home(request):
	if request.user.is_authenticated():
		parties = Game.objects.filter(Creator=request.user) | Game.objects.filter(Opponent=request.user)
		return render(request, 'accueil/home.html', {'liste_parties' : parties})

	else :
		return render(request, 'accueil/deco.html')
	# else :
	# 	form = AuthentificationForm()
	# 	return render(request, 'registration/login.html', {'form':form}, {'redirect_field_name':'/'})

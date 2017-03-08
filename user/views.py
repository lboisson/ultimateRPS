from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

def liste_users(request):
	#renvoie la date .... uselesss.fo, pour tester

    user = User.objects.all()
    return render(request, 'accueil/users.html', {'liste_user': user})

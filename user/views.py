from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


## renvoie la liste des users
def recherche(request):

    user = User.objects.all()
    return render(request, 'user/users.html', {'liste_user': user})


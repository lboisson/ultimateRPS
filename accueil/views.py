from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

from game.models import Game



def home(request):

    return render(request, 'accueil/home.html')
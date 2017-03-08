from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime
from django.db import models
from accueil.models import Game
from django.contrib.auth.models import User


def home(request):
    return render(request, 'accueil/home.html')


def view_all_game(request):
    #affiche la liste de tous les jeux
    parties = Game.objects.all() #selectionne toutes les parties
    return render(request, 'accueil/all_game.html', {'dernieres_parties' : parties})

def view_game(request, id_game):

    # Vue qui affiche une partie selon son identifiant
    # Son ID est le second paramètre de la fonction
    try:
        partie = Game.objects.get(pk=id_game)
    except Game.DoesNotExist:
        return render(request, 'accueil/notfound.html')

    return render(request, 'accueil/game.html', {'partie': partie})


def liste_users(request):
	#renvoie la date .... uselesss.fo, pour tester

    user = User.objects.all()
    return render(request, 'accueil/users.html', {'liste_user': user})

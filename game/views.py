from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

from game.models import Game

def view_all_game(request):
    #affiche la liste de tous les jeux
    parties = Game.objects.all() #selectionne toutes les parties
    return render(request, 'game/all_game.html', {'liste_parties' : parties})

def view_game(request, id_game):

    # Vue qui affiche une partie selon son identifiant
    # Son ID est le second paramètre de la fonction
    try:
        partie = Game.objects.get(pk=id_game)
    except Game.DoesNotExist:
        return render(request, 'game/notfound.html')

    return render(request, 'game/game.html', {'partie': partie})

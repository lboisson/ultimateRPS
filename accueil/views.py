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
    
	# Si l'ID est supérieur à 100(remplacer avec le nombre de partie), nous considérons que l'article n'existe pas
    if int(id_game) > 100:
        raise Http404

    return render(request, 'accueil/game.html', {'id_game': id_game})

def liste_users(request):
	#renvoie la date .... useless, pour tester

    user = User.objects.all() 
    return render(request, 'accueil/users.html', {'liste_user': user})
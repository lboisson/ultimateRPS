from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime
from accueil.models import Player
from accueil.models import Game


def home(request):
    return render(request, 'accueil/home.html')


def view_all_game(request):
    #affiche la liste de tous les jeux 
    parties = Player.objects.all() #selectionne toutes les parties
    return render(request, 'accueil/all_game.html', {'derniere_parties' : parties})    


def view_game(request, id_game):
    
    # Vue qui affiche une partie selon son identifiant
    # Son ID est le second paramètre de la fonction
    
	# Si l'ID est supérieur à 100(remplacer avec le nombre de partie), nous considérons que l'article n'existe pas
    if int(id_game) > 100:
        raise Http404

    return render(request, 'accueil/game.html', {'id_game': id_game})


def github(request):
    #redirige vers github (aucun interet, c'est pour tester la fonction)
    return redirect('https://github.com/lboisson/ultimateRPS')


def date_actuelle(request):
	#renvoie la date .... useless, pour tester
    return render(request, 'accueil/date.html', {'date': datetime.now()})
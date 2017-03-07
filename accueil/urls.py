from django.conf.urls import url
from . import views

#url des pages de l'app accueil
urlpatterns = [ 
   url(r'^$', views.home,			#vue de la homepage
    name="accueil"),

    url(r'^partie', views.view_all_game,  # Vue d'une partie
    name="all_game"),

    url(r'^partie/(\d+)$', views.view_game,  # Vue d'une partie
    name="game"),

    url(r'^github$', views.github,			#redirige sur notre git, aucun interet
    name="github"),
    
    url(r'^date$', views.date_actuelle,
    name="date"),
]
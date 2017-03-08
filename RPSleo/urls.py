"""RPSleo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from accueil import views as views_accueil
from compte import views as views_compte
from game import views as views_game


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views_accueil.home,			#vue de la homepage
    name="accueil"),
    url(r'^partie$', views_game.view_all_game,  # Vue de 50 parties
    name="all_game"),
    url(r'^partie/(\d+)$', views_game.view_game,  # Vue d'une partie
    name="game"),
    url(r'^compte$',views_compte.compte,
    name="compte"),
]

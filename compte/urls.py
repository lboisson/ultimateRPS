from django.conf.urls import url
from . import views

#url des pages de l'app accueil
urlpatterns = [
   url(r'^$', views.compte,
    name="compte"),
    url(r'^notifications', views.notifications, 
    name="notifications"),
]

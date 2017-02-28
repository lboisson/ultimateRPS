from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Bonjour, vous êtes maintenant sur la page des jeux!")


from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import ListView


## renvoie la liste des users
def recherche(request):

    user = User.objects.all()
    return render(request, 'user/users.html', {'liste_user': user})


#class UserList(ListView):
#	template_name = 'user/search.html'
#
#	def get_queryset(self):
#		query = self.request.GET.get('q')
#		return User.objects.filter(username=query)



def search(request):
	if request.GET:
		query = request.GET.get('q', None)
		results = User.objects.filter(username__icontains=query)
		return render(request, 'user/search.html', {'results':results, 'query':query})
	return render(request, 'user/search.html', {'query':query})

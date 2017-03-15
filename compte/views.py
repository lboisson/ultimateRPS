from django.shortcuts import render

def compte(request):
    return render(request, 'compte/compte.html')

def notifications(request):

	if request.user.is_authenticated():
		parties = (Game.objects.filter(Creator=request.user) | Game.objects.filter(Opponent=request.user)) 
		return render(request, 'compte/notifications.html', {'liste_parties' : parties})

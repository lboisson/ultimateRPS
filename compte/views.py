from django.shortcuts import render

def compte(request):
    return render(request, 'compte/compte.html')

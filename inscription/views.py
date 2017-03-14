from django.shortcuts import redirect, render
from .models import UserCreationForm
from inscription.models import User

def inscription(request):
    form = UserCreationForm()
    return render(request, 'base.html', {'form':form})
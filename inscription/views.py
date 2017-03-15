from django.shortcuts import redirect, render
from .models import UserCreationForm
from inscription.models import User

def inscription(request):
    form = UserCreationForm()
    return render(request, 'inscription.html', {'form':form},{'redirect_field_name':'/'})
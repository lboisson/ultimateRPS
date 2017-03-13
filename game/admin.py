from django.contrib import admin
from .models import Game

admin.site.register(Game)
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
	fields = ['PlayerOne', 'PlayerTwo', 'PlayerOneName', 'PlayerOneTwo']
	readonly=['Outcome']
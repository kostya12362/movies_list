from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from list_todo.models import Room, Chat
from list_todo.models import Rating, Movie


admin.site.register(Movie, )
admin.site.register(Rating, )
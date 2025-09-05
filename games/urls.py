# games/urls.py
from django.urls import path
from games.views import gamesAPI, gamesInfoAPI

urlpatterns = [
    path('api/games/', gamesAPI, name='gamesAPI'),
    path('api/gamesinfo/', gamesInfoAPI, name='gamesInfoAPI'),
]
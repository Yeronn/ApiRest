from django.urls import path
from .views import GameView

urlpatterns = {
    path('games/', GameView.as_view(), name = 'games_list'), #games/ es la ruta raiz que contiene todos los games y games_list es el endpoint o nombre de la url
    path('games/<int:id>', GameView.as_view(), name = 'games_process')
}
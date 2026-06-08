from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('listar/', views.list_games, name='list_games'),
    path('adicionar/', views.add_game, name='add_game'),
    path('editar/<int:id_game>/', views.edit_game, name='edit_game'),
    path('excluir/<int:id_game>/', views.delete_game, name='delete_game'),
]

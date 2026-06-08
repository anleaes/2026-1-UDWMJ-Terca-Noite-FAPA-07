from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('listar/', views.list_players, name='list_players'),
    path('adicionar/', views.add_player, name='add_player'),
    path('editar/<int:id_player>/', views.edit_player, name='edit_player'),
    path('excluir/<int:id_player>/', views.delete_player, name='delete_player'),
    path('buscar/', views.search_players, name='search_players'),
]

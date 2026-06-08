from django.urls import path
from . import views

app_name = 'supports'

urlpatterns = [
    path('listar/', views.list_supports, name='list_supports'),
    path('adicionar/', views.add_support, name='add_support'),
    path('editar/<int:id_support>/', views.edit_support, name='edit_support'),
    path('excluir/<int:id_support>/', views.delete_support, name='delete_support'),
]

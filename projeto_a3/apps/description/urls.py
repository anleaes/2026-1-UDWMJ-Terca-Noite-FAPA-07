from django.urls import path
from . import views

app_name = 'descriptions'

urlpatterns = [
    path('adicionar/', views.add_description, name='add_description'),
    path('listar/', views.list_descriptions, name='list_descriptions'),
    path('editar/<int:id_description>/', views.edit_description, name='edit_description'),
    path('excluir/<int:id_description>/', views.delete_description, name='delete_description'),
]

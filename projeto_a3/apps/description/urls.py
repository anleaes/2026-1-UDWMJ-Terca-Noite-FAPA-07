from django.urls import path
from . import views

app_name = 'descriptions'

urlpatterns = [
    path('adicionar/', views.add_description, name='add_description'),
]

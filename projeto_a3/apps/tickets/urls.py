from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('<int:ticket_id>/', views.view_ticket, name='view_ticket'),
]

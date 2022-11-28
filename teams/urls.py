from django.urls import path
from .views import *


urlpatterns = [
    path('teams/', ListarSelecoes.as_view() ),
    path('teams/<team_id>/', TeamDetails.as_view()),
]
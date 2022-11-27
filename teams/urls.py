from django.urls import path
from .views import *


urlpatterns = [
    path('teams/', ListarSelecoes.as_view() )
]
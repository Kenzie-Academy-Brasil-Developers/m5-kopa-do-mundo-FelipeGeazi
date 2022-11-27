from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict
from django.shortcuts import render


# Create your views here.

class ListarSelecoes(APIView):
    def get(self, request: Request) -> Response:
        selecoes = Team.objects.all()
        lista_selecoes = []
        for selecao in selecoes:
            selecao_dict = model_to_dict(selecao)
            lista_selecoes.append(selecao_dict)

        return Response(lista_selecoes) 
    
    def post (self, request: Request) -> Response: 
        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_201_CREATED)


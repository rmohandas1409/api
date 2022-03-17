from django.contrib.sites import requests
from django.shortcuts import render

from .models import Grupo
from .serialializers import GrupoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import requests # faz requisições HTTP

def index(request):
    api = "http://localhost:8000/ramais/getGrupo"
    requisicao = requests.get(api)

    try:
        lista = requisicao.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    dicionario = {}
    for indice, valor in enumerate(lista):
        dicionario[indice] = valor

    contexto = {
        "dados" : dicionario
    }

    return render(request, "index.html", contexto)


#GET
@api_view(['GET'])
def GrupoList(request):
    grupo = Grupo.objects.all()
    serializer = GrupoSerializer(grupo, many=True)
    return Response(serializer.data)

#POST
@api_view(['POST'])
def GrupoPost(request):
    serializer = GrupoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#PUT
@api_view(['PUT'])
def GrupoPut(request, pk):
    grupo = Grupo.objects.get(id=pk)
    serializer = GrupoSerializer(grupo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE
@api_view(['DELETE'])
def GrupoDelete(request, pk):
    grupo = Grupo.objects.get(id=pk)
    grupo.delete()
    return Response('Dados apagados!')
from django.urls import path
from . import views

urlpatterns =[
    path('getGrupo', views.GrupoList, name='listagem'),
    path('postGrupo/', views.GrupoPost, name='envio'),
    path('putGrupo/<str:pk>', views.GrupoPut, name='atualizar'),
    path('deleteGrupo/<str:pk>', views.GrupoDelete, name='deletar'),

    path('', views.index, name='index'),
]
from ramais.models import Grupo, Contato, Telefone, Email
from rest_framework import serializers

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ['id', 'nome', 'descricao']
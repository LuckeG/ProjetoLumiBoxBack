from rest_framework import serializers

from .models import Usuario
from .models import Obra
from .models import Filme
from .models import Serie


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            "nome",
            "email",
        )

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = (
            "titulo",
            "descricao",
            "ano_lancamento",
        )

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = (
            "duracao"
        )

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = (
            "qtd_episodios",
            "qtd_temporadas",
        )
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

#from .models import Usuario
from .models import Indicacao, ListaUsuario


class DjangoUserSerializer(serializers.ModelSerializer):
    foto = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password"
            "foto"
        )

class IndicacaoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(read_only=True)
    usuario_destino = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Indicacao
        fields = "__all__"


class ListaUsuarioSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = ListaUsuario
        fields = '__all__'

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



# Create your models here.

class Indicacao(models.Model):
	item_id = models.IntegerField()
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	usuario_destino = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='indicacoes_recebidas', null = True, blank = True)
	data_criacao = models.DateTimeField(auto_now_add=True)

class ListaUsuario(models.Model):
	item_id = models.IntegerField()
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	tipo = models.CharField(max_length=10)
	data_adicao = models.DateTimeField(auto_now_add=True)

class Usuario(AbstractUser):
    foto = models.ImageField(upload_to='usuarios/fotos/', null=True, blank=True)

    def __str__(self):
        return self.username

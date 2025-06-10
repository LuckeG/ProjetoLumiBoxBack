from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


class Genero(models.Model):
	nome = models.CharField(max_length=30)

	def __str__(self):
		return f"{self.nome}"
	

class Obra(models.Model):
	#Id_obra = models.IntegerField()
	titulo = models.CharField(max_length=50)
	descricao = models.CharField(max_length=60)
	ano_lancamento = models.IntegerField()

	#genero = models.ManyToManyField(
		#Genero, blank=False,null=False
	#)

	def __str__(self):
		return f"{self.titulo}"


class Filme(models.Model):
	duracao = models.IntegerField()

	def __str__(self):
		return f"{self.duracao}"


class Serie(models.Model):
	qtd_episodios = models.IntegerField()
	qtd_temporadas = models.IntegerField()

	def __str__(self):
		return f"{self.qtd_episodios}"


class Usuario(models.Model):
	nome = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	senha = models.CharField(max_length=30)

	def __str__(self):
		return f"{self.nome}"

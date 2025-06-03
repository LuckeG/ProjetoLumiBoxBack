from django.contrib.auth import get_user_model
from django.db import models


class Recado(models.Model):
	autor = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
	mensagem = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	publicado = models.BooleanField(default=False)

def _str_(self):
	return self.mensagem

# Create your models here.

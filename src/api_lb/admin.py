from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()

# Register your models here.

from .models import Usuario, Indicacao

admin.site.register (Indicacao)
admin.site.register (Usuario)
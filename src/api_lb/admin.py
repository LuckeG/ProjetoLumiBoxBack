from django.contrib import admin

# Register your models here.

from .models import Genero, Obra, Filme, Serie, Usuario


admin.site.register (Genero)
admin.site.register (Obra)
admin.site.register (Filme)
admin.site.register (Serie)
admin.site.register (Usuario)
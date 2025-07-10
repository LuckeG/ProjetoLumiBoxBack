from django.apps import AppConfig


class MuralConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_lb'

# apps.py
def ready(self):
    import api_lb.signals


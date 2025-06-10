from rest_framework import viewsets, filters
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Create your views here.

from django.urls import include, path
from rest_framework import routers
from api_lb.views import UsuarioViewSet 

router = routers.DefaultRouter()

router.register(r'auth/user', UsuarioViewSet, basename='user')

urlpatterns = [
    path("", include(router.urls)),
]
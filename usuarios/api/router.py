from django.urls import path
from rest_framework.routers import DefaultRouter
from usuarios.api.views import UsuarioApiViewSet, UsuarioView

router_usuarios = DefaultRouter()

router_usuarios.register(
    prefix='usuarios', basename='usuarios', viewset=UsuarioApiViewSet
    )

urlpatterns = [
    path('auth/me/', UsuarioView.as_view()),
]
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


from usuarios.models import Usuario
from usuarios.api.serializers import UsuarioSerializer


class UsuarioApiViewSet(ModelViewSet):
    permission_class = [IsAdminUser]
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password

        return super().update(request, *args, **kwargs)


class UsuarioView(APIView):
    permission_class = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UsuarioSerializer

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return Response(UsuarioSerializer(user).data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)

from rest_framework import generics, status

class RegistroView(generics.CreateAPIView):
    serializer_class = UsuarioSerializer
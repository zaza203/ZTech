from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout


class UserLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email = email, password = password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user = user)
            return Response({'token': token.key}, status = status.HTTP_200_OK)
        
        else:
            return Response({'error': 'Invalid credentials'}, status = status.HTTP_401_UNAUTHORIZED)
        

class UserLogout(APIView):
    authentication_classes = [SessionAuthentication, BaseAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status = status.HTTP_200_OK)
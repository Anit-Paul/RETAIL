from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, changepasswordSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
#token
from rest_framework_simplejwt.tokens import RefreshToken
#Generate tokens manually for a user
def get_tokens_for_user(user):

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
    
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({"token": token, "message":"User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                # Perform login and return a success response
                token=get_tokens_for_user(user)
                return Response({"token": token, "message":"Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class profileView(APIView):
    parser_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        serializer=UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)

class updatepasswordView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        user=request.user
        serializer=changepasswordSerializer(data=request.data,context={'user':user})
        if serializer.is_valid():
            return Response({"message":"Password updated successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
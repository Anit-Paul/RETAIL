from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class RegisterView(APIView):
    def post(self, request):
        # Handle user registration logic here
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
    def get(self, request):
        # Handle GET request logic here (if needed)
        return Response({"message": "This is the registration endpoint."}, status=status.HTTP_200_OK)
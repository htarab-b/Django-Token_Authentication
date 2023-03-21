from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import SignupSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
class SignUpView(generics.GenericAPIView):
    serializer_class = SignupSerializer
    
    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {"message": "User created successfully"}

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors)
    
class LoginView(APIView):
    def get(self, request: Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK)
    
    def post(self, request: Request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            response = {
                "message": "Login Successful",
                "token": user.auth_token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            response = {
                "error": "Invalid credentials"
            }
            return Response(data=response)
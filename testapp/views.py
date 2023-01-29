from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

def get_token(user):
    refresh= RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegistrationAPI(APIView):
    def post(self,request):
        Serializer = UseregistrationSerializer(data = request.data)
        if Serializer.is_valid():
            users = Serializer.save()
            token = get_token(users)
            return Response({"token":token, "msg":"user registration successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"msg":"invalid form data"}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    def post(self, request):
        Serializer = UserLoginSerializer(data = request.data)
        if Serializer.is_valid(raise_exception=True):
            email = Serializer.data.get("email")
            password = Serializer.data.get('password')
            user = UserRegistration.objects.filter(email=email, password=password).first()
            if user:
                token = get_token(user)   
                return Response({"token":token,"msg":"user login successfully"},status=status.HTTP_200_OK)
            else:
                return Response({"msg":"Invalid data "},status=status.HTTP_400_BAD_REQUEST)
        return Response(Serializer.errors,status=status.HTTP_400_BAD_REQUEST)

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated   

class ChangePasswordAPI(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = UserRegistration
    # permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutAPI(APIView):
    def post(request):
        request.session.clear()
        return Response({"msg":"logout successfully"},status=status.HTTP_200_OK)    
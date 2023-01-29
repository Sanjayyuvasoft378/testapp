from rest_framework import serializers
from .models import *

class UseregistrationSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model = UserRegistration
        fields = ['username','firstName','lastName','email','password','confirmPassword']
    def validate(self, attrs):
        password = attrs.get('password')
        confirmPassword = attrs.get('confirmPassword')
        if password != confirmPassword:
            raise serializers.ValidationError("password and confirm password does not match")
        return attrs


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = UserRegistration
        fields = ['email','password']

from rest_framework import serializers
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


    
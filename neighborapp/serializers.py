from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


# models serializers
class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    business=BusinessSerializer(many=True, read_only=True)
    class Meta:
        model = User
        exclude = ['neighborhood']

class NeighbourhoodSerializer(serializers.ModelSerializer):
    users=UserSerializer(many=True, read_only=True)
    business=BusinessSerializer(many=True, read_only=True)
    class Meta:
        model = Neighbourhood
        fields='__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField(
        min_length=8,
        max_length=20,
        write_only=True,
        error_messages={
            "min_length": "Password should be atleast {min_length} characters"
        }

    )
    confirmpassword=serializers.CharField(
        min_length=8,
        max_length=20,
        write_only=True,
        error_messages={
            "min_length": "Password should be atleast {min_length} characters"
        }
    )

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]

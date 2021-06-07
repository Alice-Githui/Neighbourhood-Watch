from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


# models serializers
class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        exclude =['user', 'neighbourhood']
        # fields=['name', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    business=BusinessSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        exclude = ['neighbourhood']

class NeighbourhoodSerializer(serializers.ModelSerializer):
    users=ProfileSerializer(many=True, read_only=True)
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
        fields=["username", "email", "password", "confirmpassword"]

    def create(self, validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField(
        min_length=8,
        max_length=20,
        write_only=True,
        error_messages={
            "min_length": "Password should be atleast {min_length} characters"
        }

    )
    class Meta:
        model=User
        fields=["username", "password"]

class PostSerializer(serializers.ModelSerializer):
   class Meta:
       model=Post
       fields="__all__"

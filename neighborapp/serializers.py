from rest_framework import serializers
from .models import *


# models serializers
class BusinessSerializers(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    business=BusinessSerializers(many=True, read_only=True)
    class Meta:
        model = User
        exclude = ['neighborhood']

class NeighbourhoodSerializer(serializers.ModelSerializer):
    users=UserSerializer(many=True, read_only=True)
    business=BusinessSerializers(many=True, read_only=True)
    class Meta:
        model = Neighbourhood
        fields='__all__'


from rest_framework import serializers
from .models import *

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'sport', 'language', 'programming_language',
                  'interest')


class Sport_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('id', 'name')

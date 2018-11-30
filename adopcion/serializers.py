from .models import Dog, User
from rest_framework import serializers

class DogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = ('photo','name', 'race', 'description', 'state')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','password', 'admin')


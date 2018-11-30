from rest_framework import viewsets
from .models import Dog, User
from .serializers import DogSerializer, UserSerializer
from django.shortcuts import render, get_object_or_404


class DogList(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

class UserRegister(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

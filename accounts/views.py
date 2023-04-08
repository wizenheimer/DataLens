from django.shortcuts import render
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from .serializers import ProfileSerializer, ProfileSerializerVerbose
from .models import User


class ProfileListView(ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()


class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializerVerbose
    queryset = User.objects.all()

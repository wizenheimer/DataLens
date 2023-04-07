from django.shortcuts import render
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from .serializers import DataSourceSerializer
from .models import DataSource

class DataSourceDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DataSourceSerializer
    queryset = DataSource.objects.all()

class DataSourceListView(ListCreateAPIView):
    serializer_class = DataSourceSerializer
    queryset = DataSource.objects.all()
from django.shortcuts import render
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from .serializers import (
    DataSourceSerializer,
    SchemaSerializer,
    TableSerializer,
    ColumnSerializer,
)
from .models import DataSource, Schema, Column, Table


class DataSourceDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DataSourceSerializer
    queryset = DataSource.objects.all()


class DataSourceListView(ListCreateAPIView):
    serializer_class = DataSourceSerializer
    queryset = DataSource.objects.all()


class SchemaDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SchemaSerializer
    queryset = Schema.objects.all()


class SchemaListView(ListCreateAPIView):
    serializer_class = SchemaSerializer
    queryset = Schema.objects.all()


class TableDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()


class TableListView(ListCreateAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()


class ColumnDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ColumnSerializer
    queryset = Column.objects.all()


class ColumnListView(ListCreateAPIView):
    serializer_class = ColumnSerializer
    queryset = Column.objects.all()

from rest_framework import serializers
from .models import DataSource, Schema, Table, Column, Dataset


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = "__all__"


class TableSerializer(serializers.ModelSerializer):
    column = serializers.SerializerMethodField("get_columns", read_only=True)

    class Meta:
        model = Table
        fields = "__all__"

    def get_columns(self, instance):
        return Column.objects.filter(table=instance).values()


class SchemaSerializer(serializers.ModelSerializer):
    table = serializers.SerializerMethodField("get_tables", read_only=True)

    class Meta:
        model = Schema
        fields = "__all__"

    def get_tables(self, instance):
        return Table.objects.filter(schema=instance).values()


class DataSourceSerializer(serializers.ModelSerializer):
    # schema = SchemaSerializer()
    schema = serializers.SerializerMethodField("get_schemas", read_only=True)

    class Meta:
        model = DataSource
        fields = "__all__"

    def get_schemas(self, instance):
        return Schema.objects.filter(datasource=instance).values()


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = "__all__"

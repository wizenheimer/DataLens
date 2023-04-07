from django.shortcuts import render, get_object_or_404
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_pandas import PandasSimpleView
from django.core.files import File
import pandas as pd
from pandas_profiling import ProfileReport
from django.contrib.sites.shortcuts import get_current_site
from .serializers import (
    DataSourceSerializer,
    DatasetSerializer,
    SchemaSerializer,
    TableSerializer,
    ColumnSerializer,
)
from .models import DataSource, Dataset, Schema, Column, Table


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


class DatasetListView(ListCreateAPIView):
    serializer_class = DatasetSerializer
    queryset = Dataset.objects.all()


class DatasetDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DatasetSerializer
    queryset = Dataset.objects.all()


@api_view(["GET"])
def DatasetReportView(request, pk):
    description = request.data.get("description", "")
    copyright_holder = request.data.get("copyright_holder", "")
    copyright_owner = request.data.get("copyright_owner", "")
    mode = request.data.get("mode", "minimal") == "minimal"

    dataset = get_object_or_404(Dataset, pk=pk)
    df = pd.read_csv(dataset.data)

    profile = ProfileReport(
        df,
        minimal=mode,
        title=dataset.title,
        dataset={
            "description": f"{description}",
            "copyright_holder": f"{copyright_holder}",
            "copyright_year": f"{copyright_owner}",
        },
        html={
            "style": {"full_width": True},
        },
    )

    profile.to_file(output_file=f"static/dataset-report-{pk}.html")
    with open(f"static/dataset-report-{pk}.html", "rb") as f:
        report = File(f)
        dataset.report = report
        dataset.save()
    current_site = get_current_site(request).domain
    return Response({"report": "http://" + current_site + dataset.report.url})


class DatasetFetchFrame(PandasSimpleView):
    def get_data(self, request, pk, *args, **kwargs):
        dataset = get_object_or_404(Dataset, pk=pk)
        return pd.read_csv(dataset.data)

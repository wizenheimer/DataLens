from django.urls import path
from .views import (
    DataSourceDetailView,
    DataSourceListView,
    SchemaListView,
    SchemaDetailView,
    TableListView,
    TableDetailView,
    ColumnListView,
    ColumnDetailView,
    DatasetListView,
    DatasetDetailView,
    DatasetReportView,
    DatasetFetchFrame,
)

urlpatterns = [
    # data source view
    path("<int:pk>/", DataSourceDetailView.as_view(), name="datasource_detail"),
    path("", DataSourceListView.as_view(), name="datasource_list"),
    # schema view
    path("schema/<int:pk>/", SchemaDetailView.as_view(), name="schema_detail"),
    path("schema/", SchemaListView.as_view(), name="schema_list"),
    # table view
    path("table/<int:pk>/", TableDetailView.as_view(), name="table_detail"),
    path("table/", TableListView.as_view(), name="table_list"),
    # column view
    path("column/<int:pk>/", ColumnDetailView.as_view(), name="column_detail"),
    path("column/", ColumnListView.as_view(), name="column_list"),
    # dataset view
    path("dataset/<int:pk>/", DatasetDetailView.as_view(), name="dataset_detail"),
    path("dataset/<int:pk>/dataframe/", DatasetFetchFrame, name="dataset_dataframe"),
    path("dataset/<int:pk>/report/", DatasetReportView, name="dataset_report"),
    path("dataset/", DatasetListView.as_view(), name="dataset_list"),
]

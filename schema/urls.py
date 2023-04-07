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
]

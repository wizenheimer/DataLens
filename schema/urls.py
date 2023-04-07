from django.urls import path
from .views import (
    DataSourceDetailView,
    DataSourceListView,
)

urlpatterns = [
    path("<int:pk>/", DataSourceDetailView.as_view(), name="datasource_detail"),
    path("", DataSourceListView.as_view(), name="datasource_list"),
]

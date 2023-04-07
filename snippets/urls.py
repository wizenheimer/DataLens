from django.urls import path
from .views import (
    SnippetListView,
    SnippetDetailView,
)

urlpatterns = [
    path("<int:pk>/", SnippetDetailView.as_view(), name="snippet_detail"),
    path("", SnippetListView.as_view(), name="snippet_list"),
]

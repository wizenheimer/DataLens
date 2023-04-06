from django.urls import path
from .views import (
    SnippetListView,
    SnippetDetailView,
    FolderListView,
    FolderDetailView,
)

urlpatterns = [
    path("folder/<int:pk>/", FolderDetailView.as_view(), name="snippet_list"),
    path("folder/", FolderListView.as_view(), name="snippet_list"),
    path("<int:pk>/", SnippetDetailView.as_view(), name="snippet_detail"),
    path("", SnippetListView.as_view(), name="snippet_list"),
]

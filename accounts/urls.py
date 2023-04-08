from django.urls import path
from .views import (
    ProfileListView,
    ProfileDetailView,
)

urlpatterns = [
    path("<int:pk>/", ProfileDetailView.as_view(), name="snippet_detail"),
    path("", ProfileListView.as_view(), name="snippet_list"),
]

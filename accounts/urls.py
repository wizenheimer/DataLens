from django.urls import path
from .views import (
    ProfileListView,
    ProfileDetailView,
)

urlpatterns = [
    path("<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("", ProfileListView.as_view(), name="profile_list"),
]

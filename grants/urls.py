from django.urls import path
from .views import (
    GrantView,
)

urlpatterns = [
    path("", GrantView.as_view(), name="grant_view"),
]

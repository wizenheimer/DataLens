from django.urls import path
from .views import TeamListView, TeamDetailView

urlpatterns = [
    path("<int:pk>/", TeamDetailView.as_view(), name="team_detail"),
    path("", TeamListView.as_view(), name="team_list"),
]

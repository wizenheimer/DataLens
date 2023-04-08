from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from .serializers import TeamSerializer

from .models import Team


class TeamListView(ListCreateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from .serializers import (
    SnippetSerializer,
)

from .models import Snippet


# Views for Snippets
class SnippetListView(ListCreateAPIView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()


class SnippetDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()

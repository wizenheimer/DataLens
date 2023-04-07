from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from .serializers import (
    SnippetSerializer,
    SnippetSerializerVerbose,
)

from .models import Snippet


# Views for Snippets
class SnippetListView(ListCreateAPIView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        show_verbose = self.request.query_params.get("show_verbose", False)
        if show_verbose:
            return SnippetSerializerVerbose
        return SnippetSerializer


class SnippetDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        show_verbose = self.request.query_params.get("show_verbose", False)
        if show_verbose:
            return SnippetSerializerVerbose
        return SnippetSerializer

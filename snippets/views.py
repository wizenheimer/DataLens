from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    GenericAPIView,
)
from .serializers import (
    SnippetSerializer,
    SnippetSerializerVerbose,
    FolderSerializer,
    FolderSerializerVerbose,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Snippet, Folder


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
    # serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        show_verbose = self.request.query_params.get("show_verbose", False)
        if show_verbose:
            return SnippetSerializerVerbose
        return SnippetSerializer


# Views for Folders
class FolderDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = FolderSerializerVerbose
    queryset = Folder.objects.all()


class FolderListView(ListCreateAPIView):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()

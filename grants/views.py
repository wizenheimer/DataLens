from rest_framework.views import APIView
from .serializers import GrantSerializer
from rest_framework.response import Response


class GrantView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = GrantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "grant": serializer.data,
            }
        )

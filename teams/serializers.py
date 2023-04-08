from rest_framework import serializers

# from accounts.serializers import UserSerializer
from accounts.models import User
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)
    class Meta:
        model = Team
        fields = [
            "title",
            "description",
            "token",
        ]

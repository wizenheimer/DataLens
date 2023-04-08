from rest_framework import serializers
from .models import User, TeamAssignment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)

    def to_representation(self, instance):
        return instance.email


class TeamAssignmentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    can_add_teammate = serializers.ReadOnlyField()
    can_remove_teammate = serializers.ReadOnlyField()

    class Meta:
        model = TeamAssignment
        fields = [
            "id",
            "can_add_teammate",
            "can_remove_teammate",
            "begin_date",
        ]


class ProfileSerializerVerbose(serializers.ModelSerializer):
    teams = TeamAssignmentSerializer(source="teamassignment_set", many=True)

    class Meta:
        model = User
        fields = [
            "email",
            "teams",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
        ]

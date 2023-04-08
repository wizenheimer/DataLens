from rest_framework import serializers
from .models import User, TeamAssignment, SnippetAssignment


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


class SnippetAssignmentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    can_view_snippet = serializers.ReadOnlyField()
    can_edit_snippet = serializers.ReadOnlyField()

    class Meta:
        model = SnippetAssignment
        fields = [
            "id",
            "can_view_snippet",
            "can_edit_snippet",
            "begin_date",
        ]


class ProfileSerializerVerbose(serializers.ModelSerializer):
    teams = TeamAssignmentSerializer(
        source="teamassignment_set", many=True, required=False
    )
    snippets = SnippetAssignmentSerializer(
        source="snippetassignment_set", many=True, required=False
    )
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = [
            "email",
            "teams",
            "snippets",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
        ]

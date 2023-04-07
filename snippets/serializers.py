from rest_framework import serializers
from .models import Snippet
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)

    def to_representation(self, instance):
        return instance.email


class SnippetSerializerVerbose(serializers.ModelSerializer):
    with_editor_access = UserSerializer(read_only=True, many=True)
    with_viewer_access = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Snippet
        fields = "__all__"

    def create(self, validated_data):
        snippet = Snippet.objects.create(**validated_data)
        snippet.save()

        return snippet

    def update(self, instance, validated_data):
        instance.label = validated_data.get("label", instance.label)
        instance.tag = validated_data.get("tag", instance.label)
        instance.content = validated_data.get("content", instance.content)
        instance.save()

        return instance


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = "__all__"

    def create(self, validated_data):
        snippet = Snippet.objects.create(**validated_data)
        snippet.save()

        return snippet

    def update(self, instance, validated_data):
        instance.label = validated_data.get("label", instance.label)
        instance.tag = validated_data.get("tag", instance.label)
        instance.content = validated_data.get("content", instance.content)
        instance.save()

        return instance

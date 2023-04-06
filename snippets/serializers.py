from rest_framework import serializers
from .models import Snippet, Folder
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)

    def to_representation(self, instance):
        return instance.email


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return ret["id"]


class FolderSerializerVerbose(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"


class SnippetSerializerVerbose(serializers.ModelSerializer):
    folder = FolderSerializer(read_only=True)

    class Meta:
        model = Snippet
        fields = "__all__"

    def create(self, validated_data):
        folder_data = validated_data["folder"]
        folder = Folder.objects.create(name=folder_data["name"])
        folder.save()

        validated_data.pop("folder")
        snippet = Snippet.objects.create(**validated_data)
        snippet.folder = folder
        snippet.save()

        return snippet

    def update(self, instance, validated_data):
        instance.label = validated_data.get("label", instance.label)
        instance.tag = validated_data.get("tag", instance.label)
        instance.content = validated_data.get("content", instance.content)
        instance.save()

        return instance


class SnippetSerializer(serializers.ModelSerializer):
    folder = FolderSerializer(read_only=True)
    with_editor_access = UserSerializer(read_only=True, many=True)
    with_viewer_access = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Snippet
        fields = "__all__"
        extra_kwargs = {
            "with_editor_access": {"required": False},
            "with_viewer_access": {"required": False},
        }

    def create(self, validated_data):
        folder_data = validated_data["folder"]
        folder = Folder.objects.create(name=folder_data["name"])
        folder.save()

        validated_data.pop("folder")
        snippet = Snippet.objects.create(**validated_data)
        snippet.folder = folder
        snippet.save()

        return snippet

    def update(self, instance, validated_data):
        instance.label = validated_data.get("label", instance.label)
        instance.tag = validated_data.get("tag", instance.label)
        instance.content = validated_data.get("content", instance.content)
        instance.save()

        return instance

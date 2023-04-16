from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import (
    force_str,
    smart_str,
    smart_bytes,
    DjangoUnicodeDecodeError,
)
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .models import User, TeamAssignment, SnippetAssignment, SchemaAssignment


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate(self, attrs):
        email = attrs.get("email", "")

        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already registered.")

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, min_length=6, max_length=400)
    password = serializers.CharField(required=True, write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "access_token", "refresh_token"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        password = attrs.get("password", "")
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed("Invalid credentials. Authenthication failed.")

        if not user.is_active:
            raise AuthenticationFailed("Account is inactive.")

        if not user.is_verified:
            raise AuthenticationFailed("Account is not verified.")

        return {
            "email": user.email,
            "access_token": user.get_access_token(),
            "refresh_token": user.get_refresh_token(),
        }


class VerifyEmailSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()

    def validate(self, attrs):
        uidb64 = attrs.get("uidb64")
        uid = smart_str(urlsafe_base64_decode(uidb64))
        token = attrs.get("token")
        user = get_object_or_404(User, id=uid)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise ValidationError("Token is invalid.")
        return attrs


class PasswordResetSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        uidb64 = attrs.get("uidb64")
        uid = smart_str(urlsafe_base64_decode(uidb64))
        token = attrs.get("token")
        user = User.objects.get(id=uid)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise ValidationError("Token is invalid.")
        return attrs


class GeneratePasswordResetToken(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get("email")
        if not User.objects.filter(email=email).exists():
            raise ValidationError("User doesnot exist.")
        return attrs


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


class SchemaAssignmentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    can_view_schema = serializers.ReadOnlyField()
    can_edit_schema = serializers.ReadOnlyField()

    class Meta:
        model = SchemaAssignment
        fields = [
            "id",
            "can_view_schema",
            "can_edit_schema",
            "begin_date",
        ]


class ProfileSerializerVerbose(serializers.ModelSerializer):
    teams = TeamAssignmentSerializer(
        source="teamassignment_set", many=True, required=False
    )
    snippets = SnippetAssignmentSerializer(
        source="snippetassignment_set", many=True, required=False
    )
    schemas = SchemaAssignmentSerializer(
        source="schemaassignment_set", many=True, required=False
    )
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = [
            "email",
            "teams",
            "snippets",
            "schemas",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
        ]

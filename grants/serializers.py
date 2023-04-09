from django.shortcuts import get_object_or_404
from rest_framework import serializers
import datetime

from accounts.models import (
    Team,
    User,
    TeamAssignment,
    SnippetAssignment,
    SchemaAssignment,
)
from snippets.models import Snippet
from schema.models import Schema


class GrantSerializer(serializers.Serializer):
    # add or remove
    grant = serializers.CharField(required=True)
    # email of receipiant
    email = serializers.EmailField(required=True)
    # id of the asset
    id = serializers.IntegerField(required=True)
    # type of grant : editor or viewer
    type = serializers.CharField(required=True)
    # asset type : team or schema or snippet
    asset = serializers.CharField(required=True)
    # whether to notify : true or false
    notify = serializers.BooleanField(default=True)

    # field validators
    def validate_grant(self, value):
        if value not in ["add", "remove"]:
            raise serializers.ValidationError("Grant is restricted to add or remove")
        return value

    def validate_type(self, value):
        if value not in ["editor", "viewer"]:
            raise serializers.ValidationError("Type is restricted to editor or viewer")
        return value

    def validate_asset(self, value):
        if value not in ["team", "schema", "snippet"]:
            raise serializers.ValidationError(
                "Asset is restricted to team or schema or snippet"
            )
        return value

    def team_grant(self, instance):
        id = instance["id"]
        email = instance["email"]
        grant = instance["grant"]
        type = instance["type"]
        notify = instance["notify"]

        team = get_object_or_404(Team, id=id)
        # fetch user or create a new user
        # send password reset email to the new user
        user = User.objects.get_or_create(email=email)[0]
        grant_state = "failed"
        if grant == "add":
            # print("add new grant")
            # add new grant
            if type == "editor":
                # print("check if assignment already exists")
                # check if assignment already exists
                if TeamAssignment.objects.filter(user=user.id, team=team.id).exists():
                    # print("if so, modify the assignment")
                    # if so, modify the assignment
                    teamassignment = TeamAssignment.objects.get(
                        user=user.id, team=team.id
                    )
                    teamassignment.can_add_teammate = True
                    teamassignment.can_edit_teammate = True
                    teamassignment.begin_date = datetime.datetime.now().date()
                    teamassignment.save()
                else:
                    # print("otherwise, create a new assignment")
                    # otherwise, create a new assignment
                    teamassignment = TeamAssignment(
                        user=user,
                        team=team,
                        can_add_teammate=True,
                        can_remove_teammate=True,
                        begin_date=datetime.datetime.now().date(),
                    )
                    teamassignment.save()
                grant_state = "editor"
            elif type == "viewer":
                # print("check if assignment already exists")
                # check if assignment already exists
                if TeamAssignment.objects.filter(user=user.id, team=team.id).exists():
                    # print("if so, modify assignment")
                    # if so, modify assignment
                    teamassignment = TeamAssignment.objects.get(
                        user=user.id, team=team.id
                    )
                    teamassignment.can_add_teammate = False
                    teamassignment.can_edit_teammate = False
                    teamassignment.begin_date = datetime.datetime.now().date()
                    teamassignment.save()
                else:
                    # print("else create new assignment")
                    # else create new assignment
                    teamassignment = TeamAssignment(
                        user=user,
                        team=team,
                        can_add_teammate=False,
                        can_remove_teammate=False,
                        begin_date=datetime.datetime.now().date(),
                    )
                    teamassignment.save()
                grant_state = "viewer"
        else:
            # print("remove grant")
            # remove grant
            if type == "editor":
                # print("check if grant already exists")
                # check if grant already exists
                if TeamAssignment.objects.filter(user=user.id, team=team.id).exists():
                    # print("modify team assignment make editor to viewer")
                    # modify team assignment make editor to viewer
                    teamassignment = TeamAssignment.objects.get(
                        user=user.id, team=team.id
                    )
                    teamassignment.can_add_teammate = False
                    teamassignment.can_edit_teammate = False
                    teamassignment.save()
                    user.save()
                grant_state = "editor"
            elif type == "viewer":
                # print("check if grant already exists")
                # check if grant already exists
                if TeamAssignment.objects.filter(user=user.id, team=team.id).exists():
                    # print("modify team assignment remove viewer grants")
                    # modify team assignment remove viewer grants
                    user.team.remove(team)
                    user.save()
                grant_state = "viewer"

        # if intent is to notify send email
        # if instance.notify:
        #     pass the grant state in the email
        #     pass

    def snippet_grant(self, instance):
        id = instance["id"]
        email = instance["email"]
        grant = instance["grant"]
        type = instance["type"]
        notify = instance["notify"]

        snippet = get_object_or_404(Snippet, id=id)
        # fetch user or create a new user
        # send password reset email to the new user
        user = User.objects.get_or_create(email=email)[0]
        grant_state = "failed"
        if grant == "add":
            # print("add new grant")
            # add new grant
            if type == "editor":
                # print("check if assignment already exists")
                # check if assignment already exists
                if SnippetAssignment.objects.filter(
                    user=user.id, snippet=snippet.id
                ).exists():
                    # print("if so, modify the assignment")
                    # if so, modify the assignment
                    snippetassignment = SnippetAssignment.objects.get(
                        user=user.id, snippet=snippet.id
                    )
                    snippetassignment.can_edit_snippet = True
                    snippetassignment.can_view_snippet = True
                    snippetassignment.begin_date = datetime.datetime.now().date()
                    snippetassignment.save()
                else:
                    # print("otherwise, create a new assignment")
                    # otherwise, create a new assignment
                    snippetassignment = SnippetAssignment(
                        user=user,
                        snippet=snippet,
                        can_edit_snippet=True,
                        can_view_snippet=True,
                        begin_date=datetime.datetime.now().date(),
                    )
                    snippetassignment.save()
                grant_state = "editor"
            elif type == "viewer":
                # print("check if assignment already exists")
                # check if assignment already exists
                if SnippetAssignment.objects.filter(
                    user=user.id, snippet=snippet.id
                ).exists():
                    # print("if so, modify assignment")
                    # if so, modify assignment
                    snippetassignment = SnippetAssignment.objects.get(
                        user=user.id, snippet=snippet.id
                    )
                    snippetassignment.can_edit_snippet = False
                    snippetassignment.can_view_snippet = False
                    snippetassignment.begin_date = datetime.datetime.now().date()
                    snippetassignment.save()
                else:
                    # print("else create new assignment")
                    # else create new assignment
                    snippetassignment = SnippetAssignment(
                        user=user,
                        snippet=snippet,
                        can_edit_snippet=True,
                        can_view_snippet=True,
                        begin_date=datetime.datetime.now().date(),
                    )
                    snippetassignment.save()
                grant_state = "viewer"
        else:
            # print("remove grant")
            # remove grant
            if type == "editor":
                # print("check if grant already exists")
                # check if grant already exists
                if SnippetAssignment.objects.filter(
                    user=user.id, snippet=snippet.id
                ).exists():
                    # print("modify snippet assignment make editor to viewer")
                    # modify snippet assignment make editor to viewer
                    snippetassignment = SnippetAssignment.objects.get(
                        user=user.id, snippet=snippet.id
                    )
                    snippetassignment.can_edit_snippet = False
                    snippetassignment.can_view_snippet = False
                    snippetassignment.save()
                    user.save()
                grant_state = "editor"
            elif type == "viewer":
                # print("check if grant already exists")
                # check if grant already exists
                if SnippetAssignment.objects.filter(
                    user=user.id, snippet=snippet.id
                ).exists():
                    # print("modify snippet assignment remove viewer grants")
                    # modify snippet assignment remove viewer grants
                    user.snippet.remove(snippet)
                    user.save()
                grant_state = "viewer"

        # if intent is to notify send email
        # if instance.notify:
        #     pass the grant state in the email
        #     pass

    def schema_grant(self, instance):
        id = instance["id"]
        email = instance["email"]
        grant = instance["grant"]
        type = instance["type"]
        notify = instance["notify"]

        schema = get_object_or_404(Schema, id=id)
        # fetch user or create a new user
        # send password reset email to the new user
        user = User.objects.get_or_create(email=email)[0]
        grant_state = "failed"
        if grant == "add":
            # print("add new grant")
            # add new grant
            if type == "editor":
                # print("check if assignment already exists")
                # check if assignment already exists
                if SchemaAssignment.objects.filter(
                    user=user.id, schema=schema.id
                ).exists():
                    # print("if so, modify the assignment")
                    # if so, modify the assignment
                    schemaassignment = SchemaAssignment.objects.get(
                        user=user.id, schema=schema.id
                    )
                    schemaassignment.can_edit_schema = True
                    schemaassignment.can_view_schema = True
                    schemaassignment.begin_date = datetime.datetime.now().date()
                    schemaassignment.save()
                else:
                    # print("otherwise, create a new assignment")
                    # otherwise, create a new assignment
                    schemaassignment = SchemaAssignment(
                        user=user,
                        schema=schema,
                        can_edit_schema=False,
                        can_view_schema=False,
                        begin_date=datetime.datetime.now().date(),
                    )
                    schemaassignment.save()
                grant_state = "editor"
            elif type == "viewer":
                # print("check if assignment already exists")
                # check if assignment already exists
                if SchemaAssignment.objects.filter(
                    user=user.id, schema=schema.id
                ).exists():
                    # print("if so, modify assignment")
                    # if so, modify assignment
                    schemaassignment = SchemaAssignment.objects.get(
                        user=user.id, schema=schema.id
                    )
                    schemaassignment.can_edit_schema = False
                    schemaassignment.can_view_schema = False
                    schemaassignment.begin_date = datetime.datetime.now().date()
                    schemaassignment.save()
                else:
                    # print("else create new assignment")
                    # else create new assignment
                    schemaassignment = SchemaAssignment(
                        user=user,
                        schema=schema,
                        can_edit_schema=False,
                        can_view_schema=False,
                        begin_date=datetime.datetime.now().date(),
                    )
                    schemaassignment.save()
                grant_state = "viewer"
        else:
            # print("remove grant")
            # remove grant
            if type == "editor":
                # print("check if grant already exists")
                # check if grant already exists
                if SchemaAssignment.objects.filter(
                    user=user.id, schema=schema.id
                ).exists():
                    # print("modify schema assignment make editor to viewer")
                    # modify schema assignment make editor to viewer
                    schemaassignment = SchemaAssignment.objects.get(
                        user=user.id, schema=schema.id
                    )
                    schemaassignment.can_edit_schema = False
                    schemaassignment.can_view_schema = False
                    schemaassignment.save()
                    user.save()
                grant_state = "editor"
            elif type == "viewer":
                # print("check if grant already exists")
                # check if grant already exists
                if SchemaAssignment.objects.filter(
                    user=user.id, schema=schema.id
                ).exists():
                    # print("modify schema assignment remove viewer grants")
                    # modify schema assignment remove viewer grants
                    user.schema.remove(schema)
                    user.save()
                grant_state = "viewer"

        # if intent is to notify send email
        # if instance.notify:
        #     pass the grant state in the email
        #     pass

    # saving instances
    def create(self, validated_data):
        asset = validated_data["asset"]

        if asset == "team":
            self.team_grant(validated_data)
        elif asset == "schema":
            self.schema_grant(validated_data)
        elif asset == "snippet":
            self.snippet_grant(validated_data)
        # return super().create(validated_data)
        return validated_data

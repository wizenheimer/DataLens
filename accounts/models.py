from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

from .managers import UserManager
from teams.models import Team
from snippets.models import Snippet
from schema.models import Schema


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, db_index=True)
    # has verified email address
    is_verified = models.BooleanField(default=False)
    # has an active account
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # team
    teams = models.ManyToManyField(Team, through="TeamAssignment")
    # editor of the snippet
    snippet_editor = models.ManyToManyField(
        Snippet, related_name="with_editor_access", through="EditorAssignment"
    )
    # viewer of the snippet
    snippet_viewer = models.ManyToManyField(
        Snippet, related_name="with_viewer_access", through="ViewerAssignment"
    )
    # editor of schema
    schema_editor = models.ManyToManyField(
        Schema, related_name="with_editor_access", through="SchemaEditorAssignment"
    )
    # viewer of schema
    schema_viewer = models.ManyToManyField(
        Schema, related_name="with_viewer_access", through="SchemaViewerAssignment"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.email)


class TeamAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # permissions
    can_add_teammate = models.BooleanField(default=True)
    can_remove_teammate = models.BooleanField(default=True)
    # join date
    begin_date = models.DateTimeField(auto_now_add=True)
    # exit date
    end_date = models.DateField(default=date(9999, 12, 31))

    def __str__(self):
        return f"team:{str(self.team.id)} user:{str(self.user.id)}"


class EditorAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    # permissions
    can_add_editor = models.BooleanField(default=True)
    can_remove_editor = models.BooleanField(default=True)

    def __str__(self):
        return f"snippet:{str(self.snippet.id)} user:{str(self.user.id)}"


class ViewerAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    # permissions
    can_add_viewer = models.BooleanField(default=True)
    can_remove_viewer = models.BooleanField(default=True)

    def __str__(self):
        return f"snippet:{str(self.snippet.id)} user:{str(self.user.id)}"


class SchemaViewerAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    # permissions
    can_add_viewer = models.BooleanField(default=True)
    can_remove_viewer = models.BooleanField(default=True)

    def __str__(self):
        return f"snippet:{str(self.schema.id)} user:{str(self.user.id)}"


class SchemaEditorAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    # permissions
    can_add_editor = models.BooleanField(default=True)
    can_remove_editor = models.BooleanField(default=True)

    def __str__(self):
        return f"snippet:{str(self.schema.id)} user:{str(self.user.id)}"

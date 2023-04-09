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
    # snippet
    snippets = models.ManyToManyField(Snippet, through="SnippetAssignment")
    # schema
    schemas = models.ManyToManyField(Schema, through="SchemaAssignment")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.email)


class SnippetAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    # permissions
    can_view_snippet = models.BooleanField(default=True)
    can_edit_snippet = models.BooleanField(default=True)
    # join date
    begin_date = models.DateTimeField(auto_now_add=True)
    # exit date
    end_date = models.DateField(default=date(9999, 12, 31))

    def __str__(self):
        return f"snippet:{str(self.snippet.id)} user:{str(self.user.id)}"


class SchemaAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    # permissions
    can_view_schema = models.BooleanField(default=True)
    can_edit_schema = models.BooleanField(default=True)
    # join date
    begin_date = models.DateTimeField(auto_now_add=True)
    # exit date
    end_date = models.DateField(default=date(9999, 12, 31))

    def __str__(self):
        return f"snippet:{str(self.schema.id)} user:{str(self.user.id)}"


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

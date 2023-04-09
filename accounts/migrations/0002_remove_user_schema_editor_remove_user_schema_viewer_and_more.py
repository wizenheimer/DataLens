# Generated by Django 4.2 on 2023-04-09 00:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("schema", "__first__"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="schema_editor",
        ),
        migrations.RemoveField(
            model_name="user",
            name="schema_viewer",
        ),
        migrations.CreateModel(
            name="SchemaAssignment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("can_view_schema", models.BooleanField(default=True)),
                ("can_edit_schema", models.BooleanField(default=True)),
                ("begin_date", models.DateTimeField(auto_now_add=True)),
                ("end_date", models.DateField(default=datetime.date(9999, 12, 31))),
                (
                    "schema",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="schema.schema"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="schema",
            field=models.ManyToManyField(
                through="accounts.SchemaAssignment", to="schema.schema"
            ),
        ),
    ]

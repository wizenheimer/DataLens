# Generated by Django 4.2 on 2023-04-09 00:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "accounts",
            "0002_remove_user_schema_editor_remove_user_schema_viewer_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="schemaviewerassignment",
            name="schema",
        ),
        migrations.RemoveField(
            model_name="schemaviewerassignment",
            name="user",
        ),
        migrations.DeleteModel(
            name="SchemaEditorAssignment",
        ),
        migrations.DeleteModel(
            name="SchemaViewerAssignment",
        ),
    ]

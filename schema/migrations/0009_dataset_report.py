# Generated by Django 4.2 on 2023-04-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schema", "0008_dataset_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataset",
            name="report",
            field=models.FileField(blank=True, upload_to=""),
        ),
    ]

from django.db import models


class Team(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    token = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

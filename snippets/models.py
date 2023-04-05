from django.db import models


class Folder(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Snippet(models.Model):
    # human readable description of the snippet
    label = models.TextField()
    # tag for the snippet
    tag = models.CharField(max_length=50)
    # content of the snippet
    content = models.TextField()
    # timestamp of the snippet
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label
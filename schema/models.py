from django.db import models


class Schema(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=250)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Column(models.Model):
    name = models.CharField(max_length=250)
    data_type = models.CharField(max_length=250)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

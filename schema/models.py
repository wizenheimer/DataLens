from django.db import models


class DataSource(models.Model):
    DATASOURCE_OPTIONS = (
        ("PostgreSQL", "PostgreSQL"),
        ("MySQL", "MySQL"),
        ("Amazon Redshift", "Amazon Redshift"),
        ("Big Query", "Big Query"),
        ("Snowflake", "Snowflake"),
        ("Excel", "Excel"),
        ("CSV", "CSV"),
    )
    # display name for the database
    name = models.CharField(max_length=250)
    url = models.URLField()
    category = models.CharField(choices=DATASOURCE_OPTIONS)
    host = models.CharField(max_length=250)
    port = models.CharField(max_length=250)
    # configuration name for the database
    database_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    # to do : hash it prior to storing
    password = models.CharField(max_length=250)
    # configuration details
    use_ssl = models.BooleanField(default=False)
    use_ssl_tunnel = models.BooleanField(default=False)
    # datasource metadata
    # datasource connection is validated
    is_verified = models.BooleanField(default=False)
    # datasource is enabled for querying
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Schema(models.Model):
    name = models.CharField(max_length=250)
    folder = models.ForeignKey(
        DataSource, null=True, blank=True, on_delete=models.DO_NOTHING
    )

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

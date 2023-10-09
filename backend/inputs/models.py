from django.db import models

class Label(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

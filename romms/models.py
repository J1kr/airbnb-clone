from django.db import models


class Room(models.Model):

    """" Room Model Definiton """

    created = models.DateTimeField()
    updated = models.DateTimeField()

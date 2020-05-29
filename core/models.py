from django.db import models


class TimeStampedModel(models.Model):

    """" Time Stamped Definiton """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meda:
        abstract = True

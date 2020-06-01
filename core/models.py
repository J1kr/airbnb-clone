from django.db import models


class TimeStampedModel(models.Model):

    """" Time Stamped Definiton """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meda:
        abstract = True

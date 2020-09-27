from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Plan(TimeStampedModel):
    SIZES = ((200, 200), (400, 400))

    name = models.CharField(max_length=20)
    thumbnail_sizes = ArrayField(models.IntegerField(choices=SIZES))
    original_link = models.BooleanField()
    expiring_link = models.BooleanField()

    def __str__(self):
        return self.name


class User(AbstractUser):
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)

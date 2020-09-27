from django.db import models
from django_extensions.db.models import TimeStampedModel
from sorl.thumbnail import ImageField


class Image(TimeStampedModel):
    image = ImageField(upload_to="images")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

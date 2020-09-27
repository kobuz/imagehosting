from django_extensions.db.models import TimeStampedModel
from sorl.thumbnail import ImageField


class Image(TimeStampedModel):
    image = ImageField(upload_to="images")

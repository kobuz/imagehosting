from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from server.apps.images.models import Image


def get_thumbnails(image):
    # todo return thumbnails according to plan
    th = get_thumbnail(image.image, "x200")
    return [th.url]


class ImageSerializer(serializers.ModelSerializer):
    thumbnails = serializers.SerializerMethodField()

    def get_thumbnails(self, obj):
        return get_thumbnails(obj)

    class Meta:
        model = Image
        fields = ["id", "thumbnails"]

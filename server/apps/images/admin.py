from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from server.apps.images.models import Image


@admin.register(Image)
class ImageAdmin(AdminImageMixin, admin.ModelAdmin):
    pass

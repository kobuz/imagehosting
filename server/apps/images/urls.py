from django.urls import path

from server.apps.images.viewsets import ImageUploadView

urlpatterns = [
    path("upload/", ImageUploadView.as_view()),
]

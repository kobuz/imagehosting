from rest_framework import views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from server.apps.images.models import Image


class ImageUploadView(views.APIView):
    parser_classes = [MultiPartParser]

    def put(self, request):
        file_obj = request.data["file"]
        Image.objects.create(image=file_obj, user=request.user)
        return Response(status=204)

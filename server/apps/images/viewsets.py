from rest_framework import views, generics
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from server.apps.images.models import Image
from server.apps.images.serializers import ImageSerializer


class ImageUploadView(views.APIView):
    parser_classes = [MultiPartParser]
    authentication_classes = [IsAuthenticated]

    def put(self, request):
        file_obj = request.data["file"]
        Image.objects.create(image=file_obj, user=request.user)
        return Response(status=204)


class ImagesViewSet(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [IsAuthenticated]

    def get_queryset(self):
        return super(ImagesViewSet, self).get_queryset().filter(user=self.request.user)

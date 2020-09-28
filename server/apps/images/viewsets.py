from rest_framework import viewsets, mixins
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import action

from server.apps.images.models import Image
from server.apps.images.serializers import ImageSerializer


class ImagesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser]

    def get_queryset(self):
        return super(ImagesViewSet, self).get_queryset().filter(user=self.request.user)

    @action(detail=False, methods=["put"])
    def upload(self, request):
        file_obj = request.data["file"]
        Image.objects.create(image=file_obj, user=request.user)
        return Response(status=204)

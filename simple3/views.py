from .serializers import JSONSerializer, TramaCortaSerializer,CompresorSerializer,ImgSerializer

from rest_framework import viewsets
from .models import JsonModel, TramaCorta,Compresores,Imagenes

class JSONViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = JsonModel.objects.all().order_by('-id')[:50]
    serializer_class = JSONSerializer

class TramaCortaViewSet(viewsets.ModelViewSet):
    queryset = TramaCorta.objects.all().order_by('-id')[:50]
    serializer_class = TramaCortaSerializer

class CompresoresViewset(viewsets.ModelViewSet):
    queryset = Compresores.objects.all().order_by('-id')[:10]
    serializer_class = CompresorSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Imagenes.objects.all().order_by('-id')[0]
    serializer_class= ImgSerializer

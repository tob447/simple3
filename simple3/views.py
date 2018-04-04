from .serializers import JSONSerializer, TramaCortaSerializer
from rest_framework import viewsets
from .models import JsonModel, TramaCorta

class JSONViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = JsonModel.objects.all().order_by('-id')[:50]
    serializer_class = JSONSerializer

class TramaCortaViewSet(viewsets.ModelViewSet):
    queryset = TramaCorta.objects.all().order_by('-id')[:50]
    serializer_class = TramaCortaSerializer

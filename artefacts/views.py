from rest_framework import generics

from .models import Artefact
from .serializers import ArtefactSerializer


class ArtefactsListView(generics.ListAPIView):
    queryset = Artefact.objects.all()
    serializer_class = ArtefactSerializer

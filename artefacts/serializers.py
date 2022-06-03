from rest_framework import serializers

from .models import Artefact


class ArtefactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artefact
        fields = "__all__"

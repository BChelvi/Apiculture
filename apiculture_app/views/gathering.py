from rest_framework import serializers, viewsets, permissions
from apiculture_app.models import Gathering

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission

class GatheringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gathering
        fields = ['date','quantity','intervention']

class GatheringFilters(filters.FilterSet):
    class Meta:
        model = Gathering
        fields = {
            'date': ['exact'],
            'quantity': ['exact'],#rajouter une recherche supérieure ou inférieure à une quantité
            'intervention': ['exact'],
        }


class GatheringViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hive to be viewed or edited.
    """
    queryset = Gathering.objects.all()
    serializer_class = GatheringSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GatheringFilters
    permission_classes = [permissions.IsAuthenticated]
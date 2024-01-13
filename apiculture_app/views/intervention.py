from rest_framework import serializers, viewsets, permissions
from apiculture_app.models import Intervention

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission
from .gathering import GatheringSerializer


class InterventionSerializer(serializers.ModelSerializer):
    gathering_extented = GatheringSerializer(source="gatherings",read_only=True)
    class Meta:
        model = Intervention
        fields = ['date','intervention_type','traitement','beehive','gatherings','gathering_extented']

class InterventionFilters(filters.FilterSet):
    class Meta:
        model = Intervention
        fields = {
            'date': ['exact'],
            'intervention_type': ['exact'],
            'traitement': ['exact'],
            'beehive': ['exact'],

        }


class InterventionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hive to be viewed or edited.
    """
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InterventionFilters
    permission_classes = [permissions.IsAuthenticated]
from rest_framework import serializers, viewsets, permissions
from apiculture_app.models import Contamination

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission

class ContaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contamination
        fields = ['type','date_start','date_end','beehive']

class ContaminationFilters(filters.FilterSet):
    class Meta:
        model = Contamination
        fields = {
            'type': ['exact'],
            'date_start': ['exact'],#rajouter une recherche supérieure ou inférieure à une date
            'date_end': ['exact'],#rajouter une recherche supérieure ou inférieure à une date
            'beehive': ['exact'],
        }


class ContaminationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hive to be viewed or edited.
    """
    queryset = Contamination.objects.all()
    serializer_class = ContaminationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContaminationFilters
    permission_classes = [permissions.IsAuthenticated]
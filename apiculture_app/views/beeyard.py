from rest_framework import serializers, viewsets, permissions
from apiculture_app.models import Beeyard

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

class BeeyardSerializer(serializers.ModelSerializer):
    # zone_extended = ZoneSerializer(source="zone", read_only=True)
    # zone_simplified = SimplifiedZoneSerializer(source="zone", read_only=True)
    class Meta:
        model = Beeyard
        fields = ['id', 'name',]

class BeeyardFilters(filters.FilterSet):
    class Meta:
        model = Beeyard
        fields = {
            'name': ['icontains', 'contains', 'exact'],

        }


class BeeyardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Beeyard.objects.all()
    serializer_class = BeeyardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BeeyardFilters
    # filterset_fields = ['zone']
from rest_framework import serializers, viewsets, permissions
from apiculture_app.models import Hive
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

class HiveSerializer(serializers.ModelSerializer):
    # zone_extended = ZoneSerializer(source="zone", read_only=True)
    # zone_simplified = SimplifiedZoneSerializer(source="zone", read_only=True)
    class Meta:
        model = Hive
        fields = ['id', 'name',]

class HiveFilters(filters.FilterSet):
    class Meta:
        model = Hive
        fields = {
            'name': ['icontains', 'contains', 'exact'],

        }


class HiveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Hive.objects.all()
    serializer_class = HiveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HiveFilters
    # filterset_fields = ['zone']
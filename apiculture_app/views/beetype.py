from rest_framework import serializers, viewsets, permissions
from apiculture_app.models import Beetype

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission

class BeetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beetype
        fields = ['name','vulgar_name']

class BeetypeFilters(filters.FilterSet):
    class Meta:
        model = Beetype
        fields = {
            'name': ['icontains', 'contains', 'exact'],
            'vulgar_name': ['icontains', 'contains', 'exact'],
        }


class BeetypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hive to be viewed or edited.
    """
    queryset = Beetype.objects.all()
    serializer_class = BeetypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BeetypeFilters
    permission_classes = [permissions.IsAuthenticated]
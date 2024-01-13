from rest_framework import serializers, viewsets, permissions
from apiculture_app.models import Beeyard
from apiculture_app.views import HiveSerializer

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission, SAFE_METHODS
# from rest_framework.decorators import action

class BeeyardSerializer(serializers.ModelSerializer):
    hives = HiveSerializer(read_only=True, many=True)
    apiculteur = serializers.CharField(source='apiculteur.email')
    class Meta:
        model = Beeyard
        fields = ['id', 'name','apiculteur','hives']

class BeeyardFilters(filters.FilterSet):
    class Meta:
        model = Beeyard
        fields = {
            'name': ['icontains', 'contains', 'exact'],
            'apiculteur': ['exact'],
            'hives' : ['exact'],
        }

class IsUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, beeyard):
        # Les requêtes en lecture sont toujours autorisées
        if request.method in SAFE_METHODS:
            return True
        # L'écriture n'est autorisée que si l'utilisateur actuel est l'apiculteur du cheptel
        return beeyard.apiculteur == request.user

class BeeyardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows beeyard to be viewed or edited.
    """
    queryset = Beeyard.objects.all()
    serializer_class = BeeyardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BeeyardFilters
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

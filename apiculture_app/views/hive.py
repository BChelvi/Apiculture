from rest_framework import serializers, viewsets, permissions
from apiculture_app.models import Hive
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .contamination import ContaminationSerializer
from .intervention import InterventionSerializer

class HiveSerializer(serializers.ModelSerializer):
    contamination_extended = ContaminationSerializer(source="contaminations",read_only=True,many=True)
    intervention_extented = InterventionSerializer(source="interventions",read_only=True,many=True)
    class Meta:
        model = Hive
        fields = ['id', 'name','bee_yard','bee_type','queen_age','contaminations','contamination_extended','interventions','intervention_extented']

class HiveFilters(filters.FilterSet):
    class Meta:
        model = Hive
        fields = {
            'name': ['icontains', 'contains', 'exact'],
            'bee_yard': ['exact'],
            'bee_type': ['exact'],
            'queen_age': ['exact'],#rajouter une recherche supérieure ou inférieure à une date
            'status': ['exact'],
        }


class IsUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, hive):
        # Les requêtes en lecture sont toujours autorisées
        if request.method in SAFE_METHODS:
            return True
        # L'écriture n'est autorisée que si l'utilisateur actuel est l'apiculteur du cheptel auquel appartient la ruche
        return hive.bee_yard.apiculteur == request.user

class HiveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hive to be viewed or edited.
    """
    queryset = Hive.objects.all()
    serializer_class = HiveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HiveFilters
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    
    
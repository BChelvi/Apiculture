from rest_framework import serializers, viewsets, permissions
from apiculture_app.models import Hive, Intervention
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .contamination import ContaminationSerializer
from .intervention import InterventionSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class HiveSerializer(serializers.ModelSerializer):
    contamination_extended = ContaminationSerializer(source="contaminations",many=True)
    intervention_extented = InterventionSerializer(source="interventions",many=True)
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

    @action(detail=True, methods=['GET','POST','PUT']) #enlever POST ET PUT
    def get_interventions(self, request, pk=None):
        hive = self.get_object()
        interventions = Intervention.objects.filter(beehive=hive)
        serializer = InterventionSerializer(interventions, many=True)
        print(request)
        return Response(serializer.data)

    # rajouter un edit_intervention
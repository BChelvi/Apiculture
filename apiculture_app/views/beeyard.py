from rest_framework import serializers, viewsets, permissions
from apiculture_app.models import Beeyard, Hive, Intervention
from apiculture_app.views import HiveSerializer
from .intervention import InterventionSerializer

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission, SAFE_METHODS
# from rest_framework.decorators import action

from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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

    @action(detail=True, methods=['GET','POST','PUT']) #enlever POST ET PUT
    def get_interventions(self, request, pk=None):
        beeyard = self.get_object()
        hives = Hive.objects.filter(bee_yard=beeyard)
        interventions = Intervention.objects.filter(beehive__in=hives)
        serializer = InterventionSerializer(interventions, many=True)
        return Response(serializer.data)
    
    # rajouter l'edition sur le modèle de get_intervention : récupérer les chagements du form dans la requête, et mettre à jour les instances du modèle Interventions avec les ids correspondantes.
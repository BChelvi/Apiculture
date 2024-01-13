from django.contrib import admin
from .models import Beetype,Beeyard,Hive,Intervention,Gathering,Contamination
from django.contrib.auth.admin import UserAdmin



# Register your models here.
# Admin pour le modèle Hive avec des filtres avancés
class HiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'bee_type', 'queen_age', 'bee_yard','status',)
    list_filter = ('bee_type',)
    search_fields = ('name', 'bee_type','bee_yard')
    
# Admin pour le modèle Beeyard avec des filtres avancés
class BeeyardAdmin(admin.ModelAdmin):
    list_display = ('name', 'apiculteur',)
    list_filter = ('apiculteur',)
    search_fields = ('name', 'apiculteur')
    
# Admin pour le modèle Beetype avec des filtres avancés
class BeetypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'vulgar_name')

# Admin pour le modèle Intervention avec des filtres avancés
class InterventionAdmin(admin.ModelAdmin):
    list_display = ('date', 'intervention_type','traitement','beehive')
    
# Admin pour le modèle Gathering avec des filtres avancés
class GatheringAdmin(admin.ModelAdmin):
    list_display = ('date', 'quantity','intervention',)
    
# Admin pour le modèle Contamination avec des filtres avancés
class ContaminationAdmin(admin.ModelAdmin):
    list_display = ('type', 'date_start','date_end','beehive')
    



# Enregistrement des modèles avec leurs configurations d'administration personnalisées
admin.site.register(Hive, HiveAdmin)
admin.site.register(Beeyard, BeeyardAdmin)
admin.site.register(Beetype, BeetypeAdmin)
admin.site.register(Intervention, InterventionAdmin)
admin.site.register(Gathering, GatheringAdmin)
admin.site.register(Contamination, ContaminationAdmin)

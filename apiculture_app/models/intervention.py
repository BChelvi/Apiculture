from django.db import models


class Intervention(models.Model):
    date = models.DateField()
    INTERVENTION_TYPES = [
        ('RCS', 'Royal Cell Supress'),
        ('HC', 'Health Check'),
        ('SD', 'Sirop Distribution'),
        ('PH', 'Pose de hausses'),
        ('D', 'Desctruction'),
        ('MAE', "Multiplication artificielle de l'essaim"),
    ]
    intervention_type = models.CharField(max_length=3, choices=INTERVENTION_TYPES)
    TRAITEMENT = [
        ('AP', 'apivar'),
        ('AO', 'acide oxalique'),
        ('AF', 'antifongique'),
    ]
    traitement = models.CharField(max_length=2, choices=TRAITEMENT, blank=True)
    beehyve = models.ForeignKey('Hyve', on_delete=models.CASCADE, related_name='interventions')
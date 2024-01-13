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
        ('R',"Récolte")
    ]
    intervention_type = models.CharField(max_length=3, choices=INTERVENTION_TYPES)
    TRAITEMENT = [
        ('AP', 'apivar'),
        ('AO', 'acide oxalique'),
        ('AF', 'antifongique'),
    ]
    traitement = models.CharField(max_length=2, choices=TRAITEMENT, blank=True)
    beehive = models.ForeignKey('Hive', on_delete=models.CASCADE, related_name='interventions')
    
    def __str__(self):
        return f"{self.date} - {self.intervention_type}- {self.beehive}"
    
    def edit_intervention(self, new_date, new_intervention_type, new_traitement):
        # Vous pouvez ajuster cette méthode selon vos besoins
        self.date = new_date
        self.intervention_type = new_intervention_type
        self.traitement = new_traitement
        self.save()
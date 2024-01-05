from django.db import models

class Contamination(models.Model):
    CONT_TYPE = [
        ('AAM', 'acarapisose des abeilles mellifères'),
        ('LAAM', 'loque américaine des abeilles mellifères'),
        ('LEAM', 'loque européenne des abeilles mellifères'),
        ('ICR', 'infestation par le petit coléoptère des ruches (Aethina tumida)'),
        ('IAT', "infestation des abeilles mellifères par l'acarien Tropilaelaps"),
        ('VAM', "varroose des abeilles mellifères."),
    ]
    type = models.CharField(max_length=3, choices=CONT_TYPE)

    date_start = models.DateField(auto_now_add=True)
    date_end = models.DateField(blank=True)
    beehyve = models.ForeignKey('Hyve', on_delete=models.CASCADE, related_name='contaminations')


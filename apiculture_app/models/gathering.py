from django.db import models


class Gathering(models.Model):
    date = models.DateField(auto_now_add=True)
    quantity = models.FloatField()
    beehyve = models.ForeignKey('Hyve', on_delete=models.CASCADE, related_name='gatherings')
    
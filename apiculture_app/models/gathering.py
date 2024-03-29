from django.db import models
from django.db.models import SET_NULL


class Gathering(models.Model):
    date = models.DateField(auto_now_add=True)
    quantity = models.FloatField()
    intervention = models.OneToOneField('Intervention', related_name='gatherings', on_delete=SET_NULL, null=True, blank=True, default=None)
    
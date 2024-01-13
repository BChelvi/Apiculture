from django.db import models
from django.contrib.auth.models import User


class Beeyard(models.Model):
    
    name = models.CharField(max_length=100)
    apiculteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='beeyards')
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.apiculteur}"
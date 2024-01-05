from django.db import models

class Beetype(models.Model):
    name = models.CharField(max_length=100)
    vulgar_name = name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.vulgar_name}"
from django.db import models


class Hive(models.Model):
    name = models.CharField(max_length=100)
    bee_type = models.ForeignKey('Beetype', on_delete=models.CASCADE, related_name='hives')
    queen_age = models.DateField()
    bee_yard = models.ForeignKey('Beeyard', on_delete=models.CASCADE, related_name='hives')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.bee_type}"

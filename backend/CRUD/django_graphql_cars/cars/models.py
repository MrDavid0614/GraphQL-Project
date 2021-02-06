from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    year = models.DateField()

    def __str__(self):
        return self.brand

    class Meta:
        ordering = ('brand',)

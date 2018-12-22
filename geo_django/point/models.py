from django.db import models

# Create your models here.
class Xhamia(models.Model):
    emri = models.CharField(max_length=200, unique=True)
    long = models.DecimalField(max_digits=9,decimal_places=6)
    lat = models.DecimalField(max_digits=9,decimal_places=6)

    class Meta():
        verbose_name_plural = "Xhamite"

    def __str__(self):
        return self.emri

from django.contrib.gis.db import models


# Create your models here.
class Religion(models.Model):
    name = models.CharField(max_length=200,unique=True)
    location = models.PointField(srid=4326)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Religions'

class CityPark(models.Model):
    name = models.CharField(max_length=200, unique=True)
    poly_gon = models.PolygonField()

    def __str__(self):
        return self.name

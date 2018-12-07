from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100,unique=True)
    director = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Division(models.Model):
    name = models.CharField(max_length=100,unique=True)
    chief_division = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='divisions')

    def __str__(self):
        return self.name

from django.db import models

class Komuna(models.Model):
    id_komuna = models.SmallIntegerField(unique=True)
    emri_komuna = models.CharField(max_length=50,unique=True)

    def __str__(self):

        return self.emri_komuna
        return str(self.id_komuna)

class Vendi(models.Model):
    komuna = models.ForeignKey(Komuna,on_delete=models.CASCADE)
    id_vendi = models.SmallIntegerField(unique=True)
    emri_vendi = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.emri_vendi
        return str(self.id_vendi)

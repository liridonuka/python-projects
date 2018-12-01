from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    verify_email = models.EmailField()
    text = models.CharField(max_length=254)

    def __str__ (self):
        return self.name
        return self.email
        return self.text

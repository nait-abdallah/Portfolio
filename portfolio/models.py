from django.db import models

# Create your models here.
class personMain(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    details = models.CharField(max_length=5000)
    def  __str__(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

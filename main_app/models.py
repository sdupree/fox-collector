from django.db import models

# Create your models here.
class Fox(models.Model):
  name = models.CharField(max_length=20)
  species = models.CharField(max_length=20)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  def __str__(self):
    return self.name
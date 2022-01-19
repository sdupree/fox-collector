from django.db import models
from django.urls import reverse

# Create your models here.
class Fox(models.Model):
  name = models.CharField(max_length=20)
  species = models.CharField(max_length=20)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('foxes_detail', kwargs={'fox_id': self.id})

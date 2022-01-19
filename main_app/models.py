from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Fox(models.Model):
  name = models.CharField(max_length=20)
  species = models.CharField(max_length=20)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('foxes_detail', kwargs={'fox_id': self.id})
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)  


class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  # create a fox_id column in the db
  fox = models.ForeignKey(Fox, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

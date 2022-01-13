from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def foxes_index(request):
  return render(request, 'foxes/index.html', { 'foxes': foxes })


# Add the Fox class & list and view function below the imports
class Fox:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

foxes = [
  Fox('Lolo', 'tabby', 'foul little demon', 3),
  Fox('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Fox('Raven', 'black tripod', '3 legged cat', 4)
]
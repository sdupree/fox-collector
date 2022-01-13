from django.shortcuts import render
from django.http import HttpResponse
from .models import Fox

# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def foxes_index(request):
  foxes = Fox.objects.all()
  return render(request, 'foxes/index.html', { 'foxes': foxes })


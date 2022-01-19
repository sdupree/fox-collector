from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

def foxes_detail(request, fox_id):
  fox = Fox.objects.get(id=fox_id)
  return render(request, 'foxes/detail.html', { 'fox': fox })


class FoxCreate(CreateView):
  model = Fox
  fields = ['name', 'species', 'description', 'age']

class FoxUpdate(UpdateView):
  model = Fox
  fields = ['species', 'description', 'age']  # Omit 'name' to prevent updating.

class FoxDelete(DeleteView):
  model = Fox
  success_url = '/foxes/'

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Fox, Toy
from .forms import FeedingForm

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
  # instantiate FeedingForm to be rendered in the detail.html template
  feeding_form = FeedingForm()
  toys_fox_doesnt_have = Toy.objects.exclude(id__in=fox.toys.all().values_list('id'))

  return render(request, 'foxes/detail.html', {
    'fox': fox,
    'feeding_form': feeding_form,
    'toys': toys_fox_doesnt_have,
  })

class FoxCreate(CreateView):
  model = Fox
  fields = ['name', 'species', 'description', 'age']

class FoxUpdate(UpdateView):
  model = Fox
  fields = ['species', 'description', 'age']  # Omit 'name' to prevent updating.

class FoxDelete(DeleteView):
  model = Fox
  success_url = '/foxes/'

def add_feeding(request, fox_id):
  # create a ModelForm instance using the data in the posted form
  form = FeedingForm(request.POST)
  # validate the data
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.fox_id = fox_id
    new_feeding.save()
  return redirect('foxes_detail', fox_id=fox_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def assoc_toy(request, fox_id, toy_id):
  Fox.objects.get(id=fox_id).toys.add(toy_id)
  return redirect('foxes_detail', fox_id=fox_id)

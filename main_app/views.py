from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fox
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
  # Find all toys not associated with this cat.
  return render(request, 'foxes/detail.html', {
    'fox': fox,
    'feeding_form': feeding_form,
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

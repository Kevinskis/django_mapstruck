from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Conductores

# Create your views here.

def index(request):
    return render(request, 'cliente/index.html')

def nosotros(request):
    return render(request, 'cliente/nosotros.html')

def servicios(request):
    return render(request, 'cliente/servicios.html')

def registrocliente(request):
    return render(request, 'cliente/registrocliente.html')

def registroproveedor(request):
    return render(request, 'cliente/registroproveedores.html')

def homecliente(request):
    return render(request,'cliente/HomeCliente.html')

# Lista de conductores

# Detalle de un conductor
class ConductoresListView(ListView):
    model = Conductores
    template_name = 'conductores_list.html'  # Nombre del template para listar conductores
    context_object_name = 'conductores' 

# Crear un nuevo conductor
class ConductorCreateView(CreateView):
    model = Conductores
    fields = ['nombre', 'licencia', 'telefono']
    template_name = 'conductor_form.html'
    success_url = reverse_lazy('conductor_list')

# Actualizar un conductor existente
class ConductorUpdateView(UpdateView):
    model = Conductores
    fields = ['nombre', 'licencia', 'telefono']
    template_name = 'conductor_form.html'
    success_url = reverse_lazy('conductor_list')

# Eliminar un conductor
class ConductorDeleteView(DeleteView):
    model = Conductores
    template_name = 'conductor_confirm_delete.html'
    success_url = reverse_lazy('conductor_list')
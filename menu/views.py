from django.shortcuts import render, redirect
from menu.models import Plato
from menu.forms import PlatoFormulario

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def ver_platos(request):
    
    platos = Plato.objects.all()
    
    return render(request, 'menu/ver_platos.html', {'platos': platos})

@login_required
def crear_plato(request):
    
    if request.method =='POST':
        formulario = PlatoFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            plato = Plato(
                tipo_plato=datos['tipo_plato'],
                nombre_plato=datos['nombre_plato'],
                precio=datos ['precio'],
                descripcion=datos ['descripcion'],
                fecha_creacion=datos ['fecha_creacion'],
                autor=datos ['autor'],
                imagen=datos ['imagen']
            )
            plato.save()
            return redirect('ver_platos')
    
    
    formulario = PlatoFormulario()
    
    return render(request,'menu/crear_plato.html', {'formulario': formulario})



# class ListaPlatos(ListView):
#     model = Plato
#     template_name = 'menu/ver_platos_cbv.html'
    
# class CrearPlato(CreateView):
#     model = Plato
#     succes_url = 'menu/'
#     template_name = 'menu/crear_plato_cbv.html'
#     fields = ['tipo_plato', 'nombre_plato', 'precio', 'fecha_creacion']


class EditarPlato(LoginRequiredMixin, UpdateView):
    model = Plato
    success_url = '/menu/menu/'
    template_name = 'menu/editar_plato_cbv.html'
    fields = ['tipo_plato', 'nombre_plato', 'precio', 'autor', 'fecha_creacion', 'imagen', 'descripcion']
    
    
class EliminarPlato(LoginRequiredMixin, DeleteView):
    model = Plato
    success_url = '/menu/menu/'
    template_name = 'menu/eliminar_plato_cbv.html'
    
class VerPlato(DetailView):
    model = Plato
    template_name = 'menu/ver_plato.html'
    


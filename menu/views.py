from django.shortcuts import render, redirect
from menu.models import Plato
from menu.forms import PlatoFormulario

# Create your views here.
def ver_platos(request):
    
    platos = Plato.objects.all()
    
    return render(request, 'menu/ver_platos.html', {'platos': platos})


def crear_plato(request):
    
    if request.method =='POST':
        formulario = PlatoFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            plato = Plato(
                tipo_plato=datos['tipo_plato'],
                nombre_plato=datos['nombre_plato'],
                precio=datos ['precio'],
                # descripcion=datos ['descripcion'],
                fecha_creacion=datos ['fecha_creacion']
            )
            plato.save()
            return redirect('ver_platos')
    
    
    formulario = PlatoFormulario()
    
    return render(request,'menu/crear_plato.html', {'formulario': formulario})
from tkinter import PIESLICE
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
from home.models import Pedido
from django.shortcuts import render

def hola(request):
    return HttpResponse('<h1> Bienvenido </h1>')

def mi_template(request):
    
    cargar_archivo = open(r'C:\Users\mariana figueras\Desktop\Código\Proyecto Grupal\home\templates\mi_template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
        
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    
    # cargar_archivo = open(r'C:\Users\mariana figueras\Desktop\Código\Proyecto Grupal\templates\tu_template.html', 'r')
    # template = Template(cargar_archivo.read())
    # cargar_archivo.close()
    # contexto = Context({'pedido':nombre})
    # template_renderizado = template.render(contexto)
    

    template = loader.get_template('home/tu_template.html')
    template_renderizado = template.render({'pedido': nombre})
        
    return HttpResponse(template_renderizado)

def crear_pedido(request, nombre, guarnicion):
    
    pedido= Pedido(nombre=nombre, guarnicion=guarnicion, cant_porciones=random.randrange(1,99), fecha_pedido=datetime.now())
    # pedido.save()
    # template = loader.get_template('crear_pedido.html')
    # template_renderizado = template.render({'pedido': pedido})

    # return HttpResponse(template_renderizado)
    return render(request, 'home/crear_pedido.html', {'pedido' : pedido})

def ver_pedidos(request):
    pedidos= Pedido.objects.all()
    
    # template = loader.get_template('ver_pedidos.html')
    # template_renderizado = template.render({'pedido': pedidos})
    
    # return HttpResponse(template_renderizado)
    return render(request, 'home/ver_pedidos.html', {'pedidos': pedidos})

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about_us.html')

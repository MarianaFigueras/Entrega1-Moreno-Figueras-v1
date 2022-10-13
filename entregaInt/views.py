from django.http import HttpResponse
# from datetime import datetime
from django.template import Context, Template, loader
import random

def hola(request):
    return HttpResponse('<h1> Bienvenido </h1>')

def mi_template(request):
    
    cargar_archivo = open(r'C:\Users\mariana figueras\Desktop\Código\Proyecto Grupal\templates\mi_template.html', 'r')
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
    

    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'pedido': nombre})
        
    return HttpResponse(template_renderizado)
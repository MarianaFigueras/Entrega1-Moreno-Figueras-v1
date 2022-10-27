from django import forms
from ckeditor.fields import RichTextFormField

class PlatoFormulario(forms.Form):
    tipo_plato=forms.CharField(max_length=50)
    nombre_plato=forms.CharField(max_length=50)
    # descripcion=RichTextFormField(required=False)
    precio=forms.IntegerField()
    fecha_creacion=forms.DateField(required=False)
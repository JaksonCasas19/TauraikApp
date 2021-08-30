from django.shortcuts import render

from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto() #Instanciar
    return render(request, "contacto/contacto.html",{"miFormulario":formulario_contacto})

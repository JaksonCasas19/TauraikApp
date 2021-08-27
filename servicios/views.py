from django.shortcuts import render
from servicios.models import Servicio 
# Create your views here.

def servicios(request):
    servicios = Servicio.objects.all() #Importar todos los objectos guardo en Servicios
    return render(request, "servicios/servicios.html",{"servicios":servicios})
from django.shortcuts import render, HttpResponse
#Importar la clase Servicio de models.py

# Create your views here.
def home(request):
    return render(request, "ProyectoWebApp/home.html")


def tienda(request):
   return render(request, "ProyectoWebApp/tienda.html")

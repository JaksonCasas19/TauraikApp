from django.shortcuts import render
#Importar la clase Servicio de models.py

# Create your views here.
def home(request):
    return render(request, "ProyectoWebApp/home.html")

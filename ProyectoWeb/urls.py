"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
#Crear Auth para Djandgo
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('servicios.urls')),
    path('blog/', include('blog.urls')),
    path('contacto/', include('contacto.urls')),
    path('tienda/', include('tienda.urls')),

    path('carro/', include('carro.urls')),
    path('check/', include('check.urls')),
    path('capture/', include('capture.urls')),

    #path('TauraikApp/',include('TauraikApp.urls'))
    path('',include('TauraikApp.urls')),
    #Agregar la url para la autenticacion
    #path('accounts/',include('django.contrib.auth.urls'))
    path('accounts/', include('django.contrib.auth.urls')), #auth_views.LoginView.as_view()
]

from django.shortcuts import redirect, render

from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto() #Instanciar
    #Comprobar si se ha realizado un POST
    if request.method=='POST':
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid(): #Si se ha rellenado correctamente
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            #Redireccionar un parametro o un mensaje
            return redirect("/contacto/?valido")

    return render(request, "contacto/contacto.html",{"miFormulario":formulario_contacto})

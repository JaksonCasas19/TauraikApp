from django.shortcuts import redirect, render
from .forms import FormularioContacto

from django.core.mail import EmailMessage
from decouple import config

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

            email = EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n{}".format(nombre,email,contenido),"",[config('USER_EMAIL')],reply_to=[email])

            try:
                #Envia el email que se declaro en la linea 18
                email.send()
                #Redireccionar un parametro o un mensaje
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html",{"miFormulario":formulario_contacto})

from django.shortcuts import render
# Create your views here.
from capture.models import captureUser
from django.http import HttpResponse

def capture(request):
    #miListas = Check.objects.all()
    return render(request, "capture/capture.html")


def create_capture(request):
    if request.method == 'POST':
        name = request.POST['name']
        estado = request.POST['estado']
        qr = request.POST['qr']

        captureUser.objects.create(
            name = name,
            estado = estado,
            qr = qr
        )

        return HttpResponse('')


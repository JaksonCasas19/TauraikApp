from django.shortcuts import render
# Create your views here.

def capture(request):
    #miListas = Check.objects.all()
    return render(request, "capture/capture.html")

def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        texto = request.POST['texto']
        qr = request.POST['qr']
from django.shortcuts import render
# Create your views here.

def capture(request):
    #miListas = Check.objects.all()
    return render(request, "capture/capture.html")
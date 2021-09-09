from django.shortcuts import render
# Create your views here.

def check(request):
    #miListas = Check.objects.all()
    return render(request, "capture/capture.html")
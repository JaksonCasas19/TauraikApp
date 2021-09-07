from check.models import Check
from django.shortcuts import render

# Create your views here.

def check(request):
    miListas = Check.objects.all()
    return render(request, "check/check.html", {"miListas":miListas})
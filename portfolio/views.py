from django.shortcuts import render
from .models import Photo

def home(request):
    return render(request, 'home.html', {'photos': Photo.objects.all()})
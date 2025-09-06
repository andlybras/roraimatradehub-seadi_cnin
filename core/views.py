from django.shortcuts import render
from site_setup.models import HeroImage

def home(request):
    hero_images = HeroImage.objects.all()
    context = {
        'hero_images': hero_images,
    }
    return render(request, 'home.html', context)

def quero_vender(request):
    return render(request, 'quero_vender.html')
from django.shortcuts import render
from site_setup.models import HeaderLogo, HeroImage, PartnerLogo

def home(request):
    header_logos = HeaderLogo.objects.all()
    hero_images = HeroImage.objects.all()
    partner_logos = PartnerLogo.objects.all()

    context = {
        'header_logos': header_logos,
        'hero_images': hero_images,
        'partner_logos': partner_logos,
    }
    
    return render(request, 'home.html', context)

def quero_vender(request):
    partner_logos = PartnerLogo.objects.all().order_by('order')
    header_logos = HeaderLogo.objects.all()

    context = {
        'partner_logos': partner_logos,
        'header_logos': header_logos,
    }

    return render(request, 'quero_vender.html', context)
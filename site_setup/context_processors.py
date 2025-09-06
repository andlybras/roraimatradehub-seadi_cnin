from .models import HeaderLogo, PartnerLogo

def global_context(request):
    
    return {
        'header_logos': HeaderLogo.objects.all(),
        'partner_logos': PartnerLogo.objects.all().order_by('order'),
    }
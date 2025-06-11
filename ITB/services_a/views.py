from django.shortcuts import render
from services_a.models import Service

def services(request):
    services = Service.objects.all().order_by('display_order')
    featured_services = services.filter(is_featured=True)
    
    context = {
        'services': services,
        'featured_services': featured_services,
    }
    return render(request, 'services.html', context)
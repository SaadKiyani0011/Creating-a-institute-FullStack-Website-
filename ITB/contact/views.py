from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import ContactForm
from contact.models import SiteContactInfo

def contact(request):
    contact_info = SiteContactInfo.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'contact_info': contact_info
    }
    return render(request, 'contactus.html', context)
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from .forms import ContactForm

def homepage(request):
    return render(request, 'main_app/homepage.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print "message sent"
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipients = ['info@neshitje.com']
            send_mail(subject, message, sender, recipients)
        else:
            return render(request, 'main_app/contact_us.html', {'form':form})


    form = ContactForm()
    return render(request, 'main_app/contact_us.html', {'form':form})

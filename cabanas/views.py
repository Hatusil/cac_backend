from django.shortcuts import render, redirect
from .models import ContactForm

# Create your views here.

def index(request):
    return render(request, 'cabanas/index.html')

def about(request):
    return render(request, 'cabanas/about.html')

#def home(request):
    #return render(request, 'cabanas/home.html')

def terms(request):
    return render(request, 'cabanas/terms.html')

def contact(request):
    return render(request, 'cabanas/contact.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        email = request.POST['email']
        date = request.POST['date']
        guests = int(request.POST['select'])
        message = request.POST['message']

        contact_form = ContactForm(
            name=name,
            lastname=lastname,
            email=email,
            date=date,
            guests=guests,
            message=message
        )
        contact_form.save()
        return redirect('cabanas/index.html')  # Redirige a una URL de éxito
    return render(request, 'cabanas/contact.html')
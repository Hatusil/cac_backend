from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'cabanas/contact.html', {'form': form})
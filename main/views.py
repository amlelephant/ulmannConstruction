from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect

# Create your views here.


def index(request):
    return render(request, 'main/index.html')

# send email on post request


def contact(request):
    return render(request, 'main/contact.html')


# give the gallery view the images from the database
def gallery(request):
    # give the images from the gallery model to the gallery.html
    images = Gallery.objects.all()
    return render(request, 'main/gallery.html', {'images': images})


def services(request):
    return render(request, 'main/services.html')

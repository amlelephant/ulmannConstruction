from .models import *
from django.contrib import admin
from django import forms




class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

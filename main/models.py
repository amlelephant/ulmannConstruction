from django.db import models
from django.contrib import admin

# Create your models here.


class Gallery(models.Model):
    image = models.ImageField(upload_to='media\images')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    image = models.ImageField(upload_to='media\images')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from multiprocessing.sharedctypes import Value
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    #path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

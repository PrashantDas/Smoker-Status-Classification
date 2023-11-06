from django.urls import path
from .views import face, methodology, contact

urlpatterns = [
    path('', face, name='face'),
    path('methodology/', methodology, name='methodology'),
    path('contact/', contact, name='contact')
]

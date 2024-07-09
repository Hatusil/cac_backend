from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    #path('home/', views.home, name='home'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
]

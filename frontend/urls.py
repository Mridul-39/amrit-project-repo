from django.urls import path
from . import views


urlpatterns = [
    
    path('home', views.home, name="home"),
    path('contactus', views.contact, name="contactus"),
    path('getstarted',views.getstarted, name="getstarted"),
    path('aboutus',views.aboutus, name='aboutus'),
    path('services',views.services, name='services')
    ]
    

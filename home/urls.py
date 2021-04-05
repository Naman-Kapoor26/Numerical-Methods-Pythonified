from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('N_R_input',views.N_R_input,name='N_R_input'),
    path('N_R_output',views.N_R_output,name='N_R_output'),
    path('Secant_input',views.Secant_input,name='Secant_input'),
    path('Secant_output',views.Secant_output,name='Secant_output'),
    #path('Secant',views.Secant,name='Secant')
    
    
    
]
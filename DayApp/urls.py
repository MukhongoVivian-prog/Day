
from django.contrib import admin
from django.urls import path
from DayApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('myservice/', views.myservice, name='myservice'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('myportfolio/', views.myportfolio, name='myportfolio'),
    path('team/', views.team, name='team'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about-us', views.about, name='about'),
    path('links', views.links, name='links')
]
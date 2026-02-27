from django.urls import path
from . import views   # make sure you imported views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]

from django.shortcuts import render
from .models import distination
from django.contrib.auth.decorators import login_required

@login_required(login_url='account/login/')
def index(request):
    deste=distination.objects.all()
    return render(request,'index.html',{'dest':deste})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

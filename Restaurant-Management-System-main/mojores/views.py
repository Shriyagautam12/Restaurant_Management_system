from django.shortcuts import render
from django.db import connection 
from django.http import HttpResponse
# from .models import items

# Create your views here.

def goback(request):
    if 'mailing' in request.session:
        return render(request,"mainmenu.html")
    else:
        return render(request,"login.html")

def signout(request):
    if 'mailing' in request.session:
        del request.session['mailing']
    if 'mailing' in request.session:    
        return render(request,"mainmenu.html")
    else:
        return render(request,"login.html")
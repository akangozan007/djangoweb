
# Views About
from django.shortcuts import render
# import http request respon 
from django.http import HttpResponse

# Create your views here.
# Home Page untuk app /about/
def index(request):
    context = {
        'TitlePage':'Tentang Saya',
    }
    return render(request,'indexAbout.html', context)
    
# Skills Page untuk app /about/
def skills(request):
    return HttpResponse('Javascript, python, html, css, c++ & Linux')

# meminta request jika dipanggil indexnya
from django.http import HttpResponse
# Mengimport render tuk memanggil view html nya
from django.shortcuts import render

# Home
def index(request):
    # return HttpResponse("Halaman Index Contoh")
    # variable templating 
    context = {
        'TitlePage':'Selamat datang di laman depan website',
    }
    return render(request, 'Home.html', context)
# About
def me(request):
    # return HttpResponse("Halaman about Contoh")
    return render(request, 'About.html')
# Artikel
def Art(request):
    # return HttpResponse("Halaman Artikel Contoh")
    return render(request, 'Artikel.html')
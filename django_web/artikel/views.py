from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Home Page untuk app /artikel/
def index(request):
    return render(request, 'indexArtikel.html')
# Page /category/ dari app Artikel
def cat(request):
    return HttpResponse('Kategori Artikel')
"""djangoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# Menambahkan function include 
from django.conf.urls import url, include
from django.contrib import admin

# meminta request jika dipanggil indexnya
# from django.http import HttpResponse

# function jika yang dpanggil merupakan home

# Method Views untuk Homepage
from . import views
# Mengimport App sebagai Packages
from about import views as Views_About
from artikel import views as Views_Artikel

def HelloWorld(request):
   return HttpResponse("Web Django Versi 1.11")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^coba/$',HelloWorld),
    # Memanggil Url tuk homepage
    url(r'^$',views.index),
    # url(r'^about/$',views.me),
   
    # Mengimport url di projek djangoweb
    # url(r'^about/$',Views_About.index),
   
    # Mengimport url di app about
    url(r'^about/',include('about.urls')),
   
    # url(r'^artikel/$',views.Art),
    # url(r'^artikel/$',Views_Artikel.index),
   
   # Mengimport url di app artikel
    url(r'^artikel/',include('artikel.urls')),
]

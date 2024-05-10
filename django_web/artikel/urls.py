from django.conf.urls import url 
# import views punyanya artikel
from . import views
# bikin url untuk app artikel
urlpatterns = [
    url(r'^$', views.index),
    # subfolder sub aplikasi
    url(r'^category/$', views.cat),
]
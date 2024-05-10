from django.conf.urls import url 
# import views punyanya about
from . import views
# bikin url untuk app about
urlpatterns = [
    url(r'^$', views.index),
    # url /keahlian/ subfolder app about
    url(r'^keahlian/$', views.skills), 
]
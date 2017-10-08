from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index.html$', views.index, name='index'),
    url(r'^about.html$', views.about, name='about'),
	url(r'^causes.html$', views.causes, name='causes'),

]
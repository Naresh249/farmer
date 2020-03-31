from django.conf.urls import url

from . import views

urlpatterns = [ 
	url(r'^', views.Farmer.as_view(), name='farmer'),
]
from django.conf.urls import url
from TitikPoetryApp import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.MainPage, name='mainpage'),
	url('admin/', admin.site.urls),
	url(r'^TitikPoetryApp/(\d+)/$', views.ViewList, name='viewlist'),
	url(r'^TitikPoetryApp/kitalistahan_url$', views.NewList, name='newlist'),
	url(r'^TitikPoetryApp/(\d+)/addItem$', views.AddItem, name='additem'),	
]


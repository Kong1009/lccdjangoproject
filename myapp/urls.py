"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from django.views.generic import TemplateView
from myapp import views

app_name = 'myapp'

urlpatterns = [
    url(r"^index/", views.index, name="home"),
    url(r"^consumptionandsaving/", views.consumptionandsaving, name="consumptionandsaving"),
    url(r"^employment_unemployment/", views.employment_unemployment, name="employment_unemployment"),
    url(r"^cpi/", views.cpi, name="cpi"),
    url("", views.index, name='home'),
    
    
    url(r"^test/", views.test_csv),
]

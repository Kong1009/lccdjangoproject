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
    
    url(r"^population/", views.population, name = "population"),
    
    url(r"^employmentandUnemployment/", views.employmentandUnemployment, name="employmentandUnemployment"),
    
    # 就業
    url(r"^Numberofpeopleemployedbyindustry/", views.Numberofpeopleemployedbyindustry, name="Numberofpeopleemployedbyindustry"),
    
    # 消費與儲蓄
    url(r"^consumptionandsaving/", views.consumptionandsaving, name="consumptionandsaving"),
    
    # 六大消費
    url(r"^cpi/", views.cpi, name="cpi"),
    
    # 人力資源
    url(r"^humanResources/", views.humanResources, name = "humanResources"),
    url(r"^test/", views.test_csv),
    url("", views.index, name='home'),
]

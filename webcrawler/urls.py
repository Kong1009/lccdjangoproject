from django.urls import re_path as url
from django.views.generic import TemplateView
from webcrawler import views

urlpatterns = [
    
    
    url(r"^crawler_104/$", views.crawler_104),
    url(r"^crawler_yahoo/$", views.crawler_yahoo),

]

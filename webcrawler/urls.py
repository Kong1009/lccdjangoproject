from django.urls import re_path as url
from django.views.generic import TemplateView
from webcrawler import views

urlpatterns = [
    
    
    url(r"^craw104/$", views.craw104),

]

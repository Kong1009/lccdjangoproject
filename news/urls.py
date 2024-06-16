from django.urls import re_path as url
from django.views.generic import TemplateView
from news import views

urlpatterns = [
    # 時事
    url(r"^currentEvents/", views.currentEvents, name = "currentEvents"),
    
    # 經濟
    url(r"^economic_articles/", views.economic_articles, name="economic_articles"),
    
    # 國際
    url(r"^internationality/", views.internationality, name = "internationality"),
    
    # 國際
    url(r"^domestic/", views.domestic, name = "domestic"),
]

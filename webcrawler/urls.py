from django.urls import re_path as url
from django.views.generic import TemplateView
from webcrawler import views

urlpatterns = [
    
    
    url(r"^craw104/", views.craw104),
    # url(r'^login/', TemplateView.as_view(template_name='login.html'), name = "login"),
    # url(r"^register/", TemplateView.as_view(template_name = "register.html"), name="register"),
    # url(r"^createMember/", views.createMember, name="creatMember"),
    # url(r"^checklogin/", views.checklogin, name="checklogin"),
    # url(r"^logout/", views.logout, name="logout"),
    # url(r"^test/", views.test)
]

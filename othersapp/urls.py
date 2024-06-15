from django.urls import re_path as url
from django.views.generic import TemplateView
from othersapp import views


urlpatterns = [
    url(r"^about/", views.about, name = "about"),
    url(r"^contact/", TemplateView.as_view(template_name = "contact.html"), name="contact"),
    url(r"^contactform/", views.contactform, name="contactform"),
    url(r"^test/", views.test),
]

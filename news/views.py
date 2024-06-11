from django.shortcuts import render
from .models import News

# Create your views here.
def economic_articles(request):
    data = News.objects.all()
    
    return render(request, "economy.html", {"data": data})


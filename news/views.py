from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News

# Create your views here.
def economic_articles(request):
    data = News.objects.order_by("?")
    
    
    
    
    # 分頁
    paginator = Paginator(data, 20)
    page = request.GET.get('page')
    venues = paginator.get_page(page)
    nums = 'a' * venues.paginator.num_pages
    
    try:
        datapages = paginator.page(page)
    except PageNotAnInteger:
        datapages = paginator.page(1)
    except EmptyPage:
        datapages = paginator.page(paginator).num_pages
        
        
    all_page = paginator.get_page(page)

    
    return render(request, "economy.html", {"data": data, "venues": venues, "nums": nums, "datapages":datapages})


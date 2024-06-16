from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News

# 經濟
def economic_articles(request):
    data = News.objects.filter(classification = "經濟").order_by("-date")
    
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
    # return render(request, "test.html", {"data":data})


# 時事
def currentEvents(request):
    data = News.objects.filter(classification = "時事").order_by("-date")
    
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

    
    return render(request, "currentEvents.html", {"data": data, "venues": venues, "nums": nums, "datapages":datapages})

# 國際
def internationality(request):
    data = News.objects.filter(classification = "國際").order_by("-date")
    
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

    
    return render(request, "internationality.html", {"data": data, "venues": venues, "nums": nums, "datapages":datapages})

# 國內
def domestic(request):
    data = News.objects.filter(classification = "國內").order_by("-date")
    
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

    
    return render(request, "domestic.html", {"data": data, "venues": venues, "nums": nums, "datapages":datapages})


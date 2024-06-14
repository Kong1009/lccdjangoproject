from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver #匯入 webdriver 模組
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep
from news.models import News


def craw104(request):
    search =  request.GET.get('search', '')
        
    title_list = []
    link_list = []
    date_list = []
    imglink_list = []
    
    driver = webdriver.Chrome()
    
    for i in range(1, 3):    
        url = "https://vip.104.com.tw/preLogin/recruiterForum/187/{}?search={}".format(i, search)
        driver.get(url)
        
        locator = (By.CLASS_NAME, 'recruiter-forum-listitem')
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
            
        
        pageSource = driver.page_source
        soup = BeautifulSoup(pageSource, "html.parser")
        
        
    
        
        news = soup.find_all("a", class_="recruiter-forum-listitem")
        for n in news:
            titles = n.select("h3.list__title")
            times = n.select("div.info__date")
            imglink = n.select("img.img-fluid")
            
            link_list.append("https://vip.104.com.tw"+n.get("href"))
            for t in titles:
                title_list.append(t.text)
                
            for time in times:
                date_list.append(time.text.strip())
                
            for img in imglink:
                imglink_list.append(img.get("src"))
                
    
        
        
    # 將資料存儲到列表中
    data_list = []
    for i in range(len(title_list)):
        if not News.objects.filter(title=title_list[i]).exists():
            news_item = News(
                title=title_list[i],
                link=link_list[i],
                date=date_list[i],
                imglink=imglink_list[i],
                platform = "104"
            )
            data_list.append(news_item)
            print(f"添加新闻: {news_item.title}")  # 调试信息
    
    # News.objects.create(data)
    if data_list:
        News.objects.bulk_create(data_list)
        print(f"成功插入{len(data_list)}")
    
    return HttpResponse("資料寫入完成")

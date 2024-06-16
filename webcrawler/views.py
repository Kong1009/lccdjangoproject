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

def crawler_yahoo(request):
    # 無頭模式
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE")
    

    search =  request.GET.get('search', '')
    newstype =  request.GET.get('newstype', '')
    driver = webdriver.Chrome(options=options)
    
    
    base_url = "https://tw.news.yahoo.com/search?p={}&fr=uh3_news_web&fr2=p%3Anews%2Cm%3Asb&.tsrc=uh3_news_web".format(search)
    
    def get_data_from_page(soup):
        products = soup.select('li.StreamMegaItem')
        for product in products:
            if len(productList) >= 30:
                break
    
            # 抓取標題及連結
            title_tag = product.select_one('h3.Mb\\(5px\\) > a')
            if title_tag:
                title = title_tag.get_text(strip=True)
                productList.append(title)
                productLinkList.append("https://tw.news.yahoo.com" + title_tag.get("href"))
                
    
            
            # 抓取圖片連結
            img_tag = product.select_one('div.H\\(0\\).Ov\\(h\\).Bdrs\\(2px\\) > img')
            if img_tag:
                img_src = img_tag.get('src').split('?')[0]
                imgLinkList.append(img_src)
            else:
                imgLinkList.append('')  # 如果沒有圖片，加入空字符串
            
    
            
            
            
            
            # time_tag = product.select_one('div[style*="color:#959595"]')
            # if time_tag:
            #     timeList.append(time_tag.get_text(strip=True))
            # else:
            #     timeList.append('')  # 如果沒有時間，加入空字符串
    
    productList = []
    productLinkList = []
    imgLinkList = []
    timeList = []
    
    try:
        while len(productList) < 30:  # 抓30筆
            driver.get(base_url)
            
            # 確保頁面加載
            WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.StreamMegaItem')))
            
            # 模擬滾動頁面
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                driver.execute_script("window.scrollBy(0, 400);")  # 滾輪向下400像素
                sleep(1)  # 等待1秒，讓新內容加載
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
    
            pageSource = driver.page_source
            soup = BeautifulSoup(pageSource, "html.parser")
            
            get_data_from_page(soup)
        
    finally:
        driver.quit()
    
    
    # 抓取時間
    for t in productLinkList:
        newd = webdriver.Chrome()
    
        
        newd.get(t)
        
        newssoup = BeautifulSoup(newd.page_source,"html.parser")
        
        time = newssoup.select_one("time")
        timeList.append(time.text.split(" ")[0].replace("年", "-").replace("月", "-").replace("日", ""))
        # print(time.text.split(" ")[0].replace("年", "-").replace("月", "-").replace("日", ""))
    
            
    
    newd.quit()
    
    # 將資料存儲到列表中
    data_list = []
    for i in range(len(productList)):
        if not News.objects.filter(title=productList[i]).exists():
            news_item = News(
                title=productList[i],
                link=productLinkList[i],
                date=timeList[i],
                imglink=imgLinkList[i],
                classification = newstype,
                platform = "yahoo新聞"
            )
            data_list.append(news_item)
            print(f"添加新闻: {news_item.title}")  # 调试信息
    
    # News.objects.create(data)
    if data_list:
        News.objects.bulk_create(data_list)
        print(f"成功插入{len(data_list)}")
    

    return HttpResponse("yahoo資料寫入完成")
    

def crawler_104(request):
    search =  request.GET.get('search', '')
    newstype =  request.GET.get('newstype', '')
    
    title_list = []
    link_list = []
    date_list = []
    imglink_list = []
    
    driver = webdriver.Chrome()
    
    for i in range(1, 2):    
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
                classification = newstype,
                platform = "104"
            )
            data_list.append(news_item)
            print(f"添加新闻: {news_item.title}")  # 调试信息
    
    # News.objects.create(data)
    if data_list:
        News.objects.bulk_create(data_list)
        print(f"成功插入{len(data_list)}")
    
    return HttpResponse("資料寫入完成")

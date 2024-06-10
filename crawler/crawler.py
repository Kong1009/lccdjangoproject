from selenium import webdriver #匯入 webdriver 模組
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import django
from time import sleep
from news.models import News
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



# 設置Django環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')
django.setup()


driver = webdriver.Chrome()
# driver = webdriver.Chrome(options=options)


# PCHOME
url = "https://vip.104.com.tw/preLogin/recruiterForum/187/1?search=%E7%B6%93%E6%BF%9F"
driver.get(url)

locator = (By.CLASS_NAME, 'recruiter-forum-list')
WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
    

pageSource = driver.page_source
soup = BeautifulSoup(pageSource, "html.parser")



title_list = []
link_list = []
date_list = []
imglink_list = []

news = soup.find_all("a", class_="recruiter-forum-listitem")
for n in news:
    titles = n.select("h3.list__title")
    times = n.select("div.info__date")
    imglink = n.select("img.img-fluid")
    
    link_list.append("https://vip.104.com.tw"+n.get("href"))
    for t in titles:
        title_list.append(t.text)
        
    for time in times:
        date_list.append(time.text)
        
    for img in imglink:
        imglink_list.append(img.get("src"))
        
        
    
        
    # for title, time in zip(titles, times):
    #     print("標題: ", title.text)
    #     print("時間: ", time.text)
    # print("連結: ", "https://vip.104.com.tw"+n.get("href"))
    # print()
        # 將數據保存到Django數據庫
    # News.objects.create(title=title_text, content='')  # content替換為實際抓取的內容


    
    

driver.quit()

# 將資料存儲到列表中
data = []
for i in range(len(title_list)):
    data.append(News(title=title_list[i], link=link_list[i], date=date_list[i], imglink=imglink_list[i]))


# for row in range(len(title_list)):
#     print("標題: {}".format(title_list[row]))
#     print("連結: {}".format(link_list[row]))
#     print("時間: {}".format(date_list[row]))
#     print("圖片連結: {}".format(imglink_list[row]))
#     print()
# try:
#     WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
    
#     # for i in range(5):
#     #     # 使用END鍵 來使用滾輪
#     #     driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#     #     sleep(1.5)
        
#     pageSource = driver.page_source
#     soup = BeautifulSoup(pageSource, "html.parser")
    
    
#     # products = soup.select("dl.col3f")
#     # productList = []
#     # productLinkList = []
#     # imgLinkList = []
#     # priceList = []
    
#     # dicts = {}
#     # conn = sqlite3.connect("database.db")
#     # sql = "create table if not exists shop (name text, shopLink text, imgLink text, price text, platform text)"
#     # cursor = conn.cursor()
#     # conn.execute(sql)
    
#     # # conn = mariadb.connect(host="192.0.2.1", port=3307,
#     # #     user="root", password="root",
#     # #     database="employees")

#     # for product in products:
#     #     titles = product.select("h5.prod_name a")
#     #     prices = product.select("span.value")
#     #     imgs = product.select("a.prod_img img")
#     #     for t, p in zip(titles, prices):
#     #         for img in imgs:
#     #             # print("商品: {}".format(t.text))
#     #             # print("連結: https:{}".format(t.get("href")))
#     #             # print("圖片: {}".format(img.get('src').split('?')[0]))
#     #             # print("價格: {:,}".format(int(p.text)))
#     #             p_link = "https:"+t.get("href")
#     #             i_link = img.get('src').split('?')[0]
                
#     #             productList.append(t.text)
#     #             productLinkList.append("https:"+t.get("href"))
#     #             imgLinkList.append(img.get('src').split('?')[0])
#     #             priceList.append(int(p.text))
#     #             dicts[t.text] = ["https:"+t.get("href"), int(p.text)]
                
#     #             # 判斷資料庫中是否有重複的資料存在
#     #             cursor.execute("select * from pchome where title = ?", [t.text])
#     #             existing_record = cursor.fetchone()
                
                
#     #             if existing_record is None:                
#     #                 try:
#     #                     sql = "insert into pchome(name, shoplink, imgLink, price, platform) values(?, ?, ?, ?, ?)"
#     #                     cursor.execute(sql, [t.text, p_link, i_link, p.text, "PcHome"])
#     #                     conn.commit()
#     #                 except:
#     #                     conn.rollback()
#     #             else:
#     #                 print("資料庫中已有資料存在")

    
# finally:
#     # conn.close()
#     driver.close()
#     # for i in range(len(productList)):
#     #     print(i+1)
#     #     print("商品: {}".format(productList[i]))
#     #     print("連結: https:{}".format(t.get("href")))
#     #     print("圖片: {}".format(imgLinkList[i]))
#     #     print("價格: {:,}".format(priceList[i]))
#     #     print()
#     # print(dicts)
    

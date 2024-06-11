from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

from .models import National_Data
from news.models import News
import pandas as pd
import json

def index(request):
    # newsdata = News.objects.all()
    newsdata = News.objects.order_by("?")[:6]

    
    return render(request, "index.html", {"newsdata": newsdata})

# 存到資料庫的用法
# def index(request):
#     data = National_Data.objects.all()
#     years = [entry.year for entry in data]
#     AverageIncomePerson_annualGrowthRate = [entry.AverageIncomePerson_annualGrowthRate for entry in data]
#     # AverageIncomePerson_annualGrowthRate = [int(entry.AverageIncomePerson_annualGrowthRate.replace(',', '')) for entry in data]
    
#     NationalIncome_nominalValue_millionYuan = [entry.AverageIncomePerson_nominalValue_millionYuan for entry in data]
#     # NationalIncome_nominalValue_millionYuan = [int(entry.AverageIncomePerson_nominalValue_millionYuan.replace(',', '')) for entry in data]
    
#     context = {
#         'years': json.dumps(years),
#         'AverageIncomePerson_annualGrowthRate': json.dumps(AverageIncomePerson_annualGrowthRate),
#         "NationalIncome_nominalValue_millionYuan": json.dumps(NationalIncome_nominalValue_millionYuan),
#         'data': data
#     }
    
#     return render(request, "test.html", context)
    # return render(request, "index.html", context)

# 就業與失業
def employment_unemployment(request):
    # 產業人數
    csv_path1 = os.path.join(settings.BASE_DIR, 'static', 'industrial_people.csv')
    # 男女就業與失業
    csv_path2 = os.path.join(settings.BASE_DIR, 'static', 'Employment and Unemployment.csv')
    

    # 读取 CSV 文件
    data1 = pd.read_csv(csv_path1, encoding="utf-8")
    data2 = pd.read_csv(csv_path2, encoding="big5", skiprows=3)
    data2.rename(columns={data2.columns[0]: 'Year'}, inplace=True)
    print(data2)
    
    data1=data1[:-2]
    data2=data2[:-5]
    # print(data1)
    
    # 就業與失業欄位整理
    data2 = data2.rename(columns={"男": "employedPopulation_male",
                                  "女": "employedPopulation_female",
                                  "男.1": "Numberofunemployed_male",
                                  "年女.1": "Numberofunemployed_female",
                                  "男.2":"manpower_male",
                                  "女.2": "manpower_female",
                                  "男.3":"unemploymentRate_male",
                                  "女.3": "unemploymentRate_female"})
    print(data2)
    # year_xlabels = data1['統計期'].tolist()
    
    # # 線條1 國民消費
    # nationalConsumption = data2["nationalConsumption"].tolist()
    
    # # 線條2
    # nationalSavings = data2["nationalSavings"].tolist()
    
    # # 線條3
    # domesticInvestment = data2["domesticInvestment"].tolist()
    
    # # 線條4 - 人均收入
    # perCapitaIncome = data1['國民所得毛額GNI(名目值，百萬元)'].tolist()
    # perCapitaIncome = [data.replace(",", "") for data in perCapitaIncome]
    
    
    # context = {
    #     "year_xlabels" : json.dumps(year_xlabels),
    #     "nationalConsumption": json.dumps(nationalConsumption),
    #     "nationalSavings": json.dumps(nationalSavings),
    #     "domesticInvestment": json.dumps(domesticInvestment),
    #     "perCapitaIncome": json.dumps(perCapitaIncome),
    #     "data1": data1.to_dict(orient="records"),
    #     "data2": data2.to_dict(orient="records")
    #     }
    return render(request, "employment_unemployment.html")

# 外部csv檔的抓取
# def index(request):
#     # 人均收入csv
#     # data1 = pd.read_csv("NationalIncomeStatistics(perCapitaIncome).csv", encoding="big5", skiprows=2)
    
#     # # 儲蓄與消費
#     # data2 = pd.read_csv("nationalIncome_SavingsAndInvestment.csv", encoding="big5", skiprows=2)
#     # data1=data1[:-2]
#     # data2=data2[:-2]
    
#     csv_path1 = os.path.join(settings.BASE_DIR, 'static', 'NationalIncomeStatistics(perCapitaIncome).csv')
#     csv_path2 = os.path.join(settings.BASE_DIR, 'static', 'nationalIncome_SavingsAndInvestment.csv')

#     # 读取 CSV 文件
#     data1 = pd.read_csv(csv_path1, encoding="big5", skiprows=2)
#     data2 = pd.read_csv(csv_path2, encoding="big5", skiprows=3)
    
#     data1=data1[:-3]
#     data2=data2[:-6]
#     # print(data2)
#     data2 = data2.rename(columns={"3.1國民消費": "nationalConsumption",
#                                   "年增率(%)": "nationalConsumption_annualGrowthRate",
#                                   "3.3國民儲蓄毛額:2.1+3.2": "nationalSavings",
#                                   "年增率(%).1": "nationalSavings_annualGrowthRate",
#                                   "3.5國內投資毛額":"domesticInvestment",
#                                   "年增率(%).2": "domesticInvestment_annualGrowthRate",})
    
#     year_xlabels = data1['統計期'].tolist()
    
#     # 線條1 國民消費
#     nationalConsumption = data2["nationalConsumption"].tolist()
    
#     # 線條2
#     nationalSavings = data2["nationalSavings"].tolist()
    
#     # 線條3
#     domesticInvestment = data2["domesticInvestment"].tolist()
    
#     # 線條4 - 人均收入
#     perCapitaIncome = data1['國民所得毛額GNI(名目值，百萬元)'].tolist()
#     perCapitaIncome = [data.replace(",", "") for data in perCapitaIncome]
    
    
#     context = {
#         "year_xlabels" : json.dumps(year_xlabels),
#         "nationalConsumption": json.dumps(nationalConsumption),
#         "nationalSavings": json.dumps(nationalSavings),
#         "domesticInvestment": json.dumps(domesticInvestment),
#         "perCapitaIncome": json.dumps(perCapitaIncome),
#         "data1": data1.to_dict(orient="records"),
#         "data2": data2.to_dict(orient="records")
#         }
#     return render(request, "index.html", context)
    # return render(request, "test.html", context)

# 六大消費之趨勢
def cpi(request):
    csv_path = os.path.join(settings.BASE_DIR, 'static', 'basicConsumerPriceIndex.csv')

    # 读取 CSV 文件
    data = pd.read_csv(csv_path, encoding="big5", skiprows=2)

    
    data=data[:-2]
    # print(data)
    data = data.rename(columns={"年增率(%)": "overallIndex_annualGrowthRate",                                
                                  "一.食物類": "food",
                                  "年增率(%).1": "foodt_annualGrowthRate",
                                  
                                  "二.衣著類":"clothing",                                  
                                  "年增率(%).2": "clothing_annualGrowthRate",
                                  
                                  "三.居住類":"residential",                                  
                                  "年增率(%).3": "residential_annualGrowthRate",
                                  
                                  "四.交通及通訊類":"transportationAndCommunications",
                                  "年增率(%).4": "transportationAndCommunications_annualGrowthRate",
                                  
                                  "五.醫藥保健類":"medicineAndHealth",
                                  "年增率(%).5": "medicineAndHealth_annualGrowthRate",
                                  
                                  "六.教養娛樂類":"educationAndEntertainment",
                                  "年增率(%).6": "educationAndEntertainment_annualGrowthRate",
                                  
                                  "七.雜項類":"miscellaneouss",
                                  "年增率(%).7": "miscellaneouss_annualGrowthRate"})
    
    year_xlabels = data['統計期'].tolist()
    
    # 線條1
    food = data["food"].tolist()
    
    # 線條2 
    clothing = data["clothing"].tolist()
    
    # 線條3
    transportationAndCommunications = data["transportationAndCommunications"].tolist()
    
    # 線條4
    medicineAndHealth = data['medicineAndHealth'].tolist()
    
    # 5
    educationAndEntertainment = data['educationAndEntertainment'].tolist()
    
    # 6
    miscellaneouss = data['miscellaneouss'].tolist()
    # perCapitaIncome = [data.replace(",", "") for data in perCapitaIncome]
    
    
    context = {
        "year_xlabels" : json.dumps(year_xlabels),
        "food": json.dumps(food),
        "clothing": json.dumps(clothing),
        "transportationAndCommunications": json.dumps(transportationAndCommunications),
        "medicineAndHealth": json.dumps(medicineAndHealth),
        "educationAndEntertainment": json.dumps(educationAndEntertainment),
        "miscellaneouss": json.dumps(miscellaneouss),
        "data": data.to_dict(orient="records")
        }
    return render(request, "cpi.html", context)

# 消費與儲蓄
def consumptionandsaving(request):
    csv_path1 = os.path.join(settings.BASE_DIR, 'static', 'NationalIncomeStatistics(perCapitaIncome).csv')
    csv_path2 = os.path.join(settings.BASE_DIR, 'static', 'nationalIncome_SavingsAndInvestment.csv')

    # 读取 CSV 文件
    data1 = pd.read_csv(csv_path1, encoding="big5", skiprows=2)
    data2 = pd.read_csv(csv_path2, encoding="big5", skiprows=3)

    data1=data1[:-3]
    data2=data2[:-6]
    # print(data2)
    data2 = data2.rename(columns={"3.1國民消費": "nationalConsumption",
                                  "年增率(%)": "nationalConsumption_annualGrowthRate",
                                  "3.3國民儲蓄毛額:2.1+3.2": "nationalSavings",
                                  "年增率(%).1": "nationalSavings_annualGrowthRate",
                                  "3.5國內投資毛額":"domesticInvestment",
                                  "年增率(%).2": "domesticInvestment_annualGrowthRate",})
    
    year_xlabels = data1['統計期'].tolist()
    
    # 線條1 國民消費
    nationalConsumption = data2["nationalConsumption"].tolist()
    
    # 線條2
    nationalSavings = data2["nationalSavings"].tolist()
    
    # 線條3
    domesticInvestment = data2["domesticInvestment"].tolist()
    
    # 線條4 - 人均收入
    perCapitaIncome = data1['國民所得毛額GNI(名目值，百萬元)'].tolist()
    perCapitaIncome = [data.replace(",", "") for data in perCapitaIncome]
    
    
    context = {
        "year_xlabels" : json.dumps(year_xlabels),
        "nationalConsumption": json.dumps(nationalConsumption),
        "nationalSavings": json.dumps(nationalSavings),
        "domesticInvestment": json.dumps(domesticInvestment),
        "perCapitaIncome": json.dumps(perCapitaIncome),
        "data1": data1.to_dict(orient="records"),
        "data2": data2.to_dict(orient="records")
        }
    return render(request, "consumptionandsaving.html", context)

def test_csv(request):
    
    # 人均收入csv
    data1 = pd.read_csv("NationalIncomeStatistics(perCapitaIncome).csv", encoding="big5", skiprows=2)
    
    # 儲蓄與消費
    data2 = pd.read_csv("nationalIncome_SavingsAndInvestment.csv", encoding="big5", skiprows=2)
    data1=data1[:-2]
    data2=data2[:-2]

    xlabels = data1['統計期'].tolist()
    values = data1['國民所得毛額GNI(名目值，百萬元)'].tolist()
    combined = zip(xlabels, values)
    
    context = {
        'labels': xlabels,
        'values': values,
    }
    return render(request, "test.html", locals())
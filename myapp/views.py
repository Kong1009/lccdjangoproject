from django.shortcuts import render
from django.conf import settings
import os
from news.models import News
import pandas as pd
import json

def index(request):

    theme_news = News.objects.order_by("?")[:5]
    newsdata = News.objects.order_by("?")[:6]

    
    return render(request, "index.html", {"newsdata": newsdata, "theme_news": theme_news})


def population(request):
    csv_path = os.path.join(settings.BASE_DIR, 'static', 'csv/人口數.csv')
    
    data = pd.read_csv(csv_path, encoding="big5", skiprows=2)
    
    data = data.rename(columns={"統計期": "year",
                                "出生人數(人) ": "Numberofbirths",
                                "出生率": "birthRate",
                                "男性出生人數(人) ": "NumberofMaleBirths",
                                "女性出生人數(人) ": "NumberofFemaleBirths",
                                "死亡人數(人) ": "NumberofDeaths",
                                "死亡率": "mortalityRate"
                                
                                
                                })
    
    year_xlabels = data["year"].to_list()
    
    Numberofbirths = data["Numberofbirths"].to_list()
    
    birthRate = data["birthRate"].to_list()
    
    NumberofMaleBirths = data["NumberofMaleBirths"].to_list()
    
    NumberofFemaleBirths = data["NumberofFemaleBirths"].to_list()
    
    NumberofDeaths = data["NumberofDeaths"].to_list()
    
    mortalityRate = data["mortalityRate"].to_list()
    
    
    data = data.to_dict(orient="records")

    context = {
        "year_xlabels" : json.dumps(year_xlabels),
        "Numberofbirths": json.dumps(Numberofbirths),
        "birthRate": json.dumps(birthRate),
        "NumberofMaleBirths": json.dumps(NumberofMaleBirths),
        "NumberofFemaleBirths": json.dumps(NumberofFemaleBirths),
        "NumberofDeaths": json.dumps(NumberofDeaths),
        "mortalityRate": json.dumps(mortalityRate),
        "data": data
        }
    
    return render(request, "population.html", {"context": context})

    

def Numberofpeopleemployedbyindustry(request): 
    # 各產業就業
    csv_path2 = os.path.join(settings.BASE_DIR, 'static', 'csv/各產業就業人口.csv')
    
    
    data = pd.read_csv(csv_path2, encoding="big5")
    # data2.rename(columns={data2.columns[0]: 'Year'}, inplace=True)
    data.drop(data.columns[-1], axis=1, inplace=True)

    
    data=data[:-2]
    # print("old: ", data)

    # 就業欄位整理
    data = data.rename(columns={"統計期": "year",
                                  "農、林、漁、牧業 ": "agriculture_forestry_fishery_animalHusbandry",
                                  "礦業及土石採取業 ": "miningIndustry",
                                  "製造業 ": "manufacturing",
                                  "電力及燃氣供應業 ": "ElectricityandGasSupplyIndustry",
                                  "用水供應及污染整治業 ": "wastewaterIndustry",
                                  "營造業 ": "constructionIndustry",
                                  "批發及零售業 ": "WholesaleandRetailTrade",
                                  "運輸及倉儲業 ": "TransportationandWarehousingIndustry",
                                  "住宿及餐飲業 ": "AccommodationandCateringUndustry",
                                  "資訊及通訊傳播業 ": "InformationandCommunicationsIndustry",
                                  "金融及保險業 ": "FinanceandInsuranceIndustry",
                                  "不動產業 ": "realEstate",
                                  "專業、科學及技術服務業 ": "ProfessionalScientificandTechnicalServices",
                                  "支援服務業 ": "SupportServiceIndustry",
                                  "公共行政及國防；強制性社會安全 ": "PublicAdministrationandDefence_MandatorySocialSecurity",
                                  "教育服務業 ": "EducationalServiceIndustry",
                                  "醫療保健及社會工作服務業 ": "HealthcareAndSocialWorkServicesIndustry",
                                  "藝術、娛樂及休閒服務業 ": "ArtsEntertainmentandLeisureServices",
                                  "其他服務業 ": "OtherServiceindustries",
    })
    
    
    year_xlabels = data['year'].astype(str).str.replace('.0', '年').tolist()


    print(year_xlabels)
    
    # 農、林、漁、牧業
    agriculture_forestry_fishery_animalHusbandry = data["agriculture_forestry_fishery_animalHusbandry"].tolist()
    
    # 礦業及土石採取業
    miningIndustry = data["miningIndustry"].tolist()
    
    # 製造業
    manufacturing = data["manufacturing"].tolist()

    # 電力及燃氣供應業
    ElectricityandGasSupplyIndustry = data['ElectricityandGasSupplyIndustry'].tolist()    
    
    # 用水供應及污染整治業
    wastewaterIndustry = data['wastewaterIndustry'].tolist()    
    
    # 營造業
    constructionIndustry = data['constructionIndustry'].tolist()    
    
    # 批發及零售業
    WholesaleandRetailTrade = data['WholesaleandRetailTrade'].tolist()    
    
    # 運輸及倉儲業
    TransportationandWarehousingIndustry = data['TransportationandWarehousingIndustry'].tolist()    
    
    # 住宿及餐飲業
    AccommodationandCateringUndustry = data['AccommodationandCateringUndustry'].tolist()    
    
    # 資訊及通訊傳播業
    InformationandCommunicationsIndustry = data['InformationandCommunicationsIndustry'].tolist()    
    
    # 金融及保險業
    FinanceandInsuranceIndustry = data['FinanceandInsuranceIndustry'].tolist()    
    
    # 不動產業
    realEstate = data['realEstate'].tolist()    
    
    # 專業、科學及技術服務業
    ProfessionalScientificandTechnicalServices = data['ProfessionalScientificandTechnicalServices'].tolist()
    
    # 支援服務業
    SupportServiceIndustry = data['SupportServiceIndustry'].tolist()    
    
    # 公共行政及國防；強制性社會安全
    PublicAdministrationandDefence_MandatorySocialSecurity = data['PublicAdministrationandDefence_MandatorySocialSecurity'].tolist()
    
    # 教育服務業
    EducationalServiceIndustry = data['EducationalServiceIndustry'].tolist()
    
    # 醫療保健及社會工作服務業
    HealthcareAndSocialWorkServicesIndustry = data['HealthcareAndSocialWorkServicesIndustry'].tolist()
    
    # 藝術、娛樂及休閒服務業
    ArtsEntertainmentandLeisureServices = data['ArtsEntertainmentandLeisureServices'].tolist()
    
    # 其他服務業
    OtherServiceindustries = data['OtherServiceindustries'].tolist()
    
    
    data = data.to_dict(orient="records")

    context = {
        "year_xlabels" : json.dumps(year_xlabels),
        # 農、林、漁、牧業
        "agriculture_forestry_fishery_animalHusbandry": json.dumps(agriculture_forestry_fishery_animalHusbandry),
        
        # 製造業
        "manufacturing": json.dumps(manufacturing),
        
        # 批發及零售業
        "WholesaleandRetailTrade": json.dumps(WholesaleandRetailTrade),
        
        # 營造業
        "constructionIndustry": json.dumps(constructionIndustry),
        
        # 住宿及餐飲業
        "AccommodationandCateringUndustry": json.dumps(AccommodationandCateringUndustry),
        
        # 教育服務業
        "EducationalServiceIndustry": json.dumps(EducationalServiceIndustry),
        
        # 運輸及倉儲業
        "TransportationandWarehousingIndustry": json.dumps(TransportationandWarehousingIndustry),
        
        # 醫療保健及社會工作服務業
        "HealthcareAndSocialWorkServicesIndustry": json.dumps(HealthcareAndSocialWorkServicesIndustry),
        
        #其他服務業
        "OtherServiceindustries": json.dumps(OtherServiceindustries),

        "data": data
        }
    

    return render(request, "employment.html", {"context": context})




def employmentandUnemployment(request): 
    # 就業與失業人數
    csv_path2 = os.path.join(settings.BASE_DIR, 'static', 'csv/EmploymentAndUnemployment.csv')
    

    # 读取 CSV 文件
    # data1 = pd.read_csv(csv_path1, encoding="utf-8")
    
    data2 = pd.read_csv(csv_path2, encoding="big5", skiprows=2)
    data2.rename(columns={data2.columns[0]: 'Year'}, inplace=True)
    
    print("old: ", data2)
    
    # data1=data1[:-2]
    # data2=data2[:-5]
    # print(data1)
    
    # 就業與失業欄位整理
    data2 = data2.rename(columns={"就業人數(千人)-合計 ": "employedPopulation",
                                  "失業人數(千人)-合計 ": "numberOfUnemployed",

    })
    # print("new: ",data2)
    year_xlabels = data2['Year'].tolist()
    print(data2.columns)
    # 線條1
    employedPopulation_male = data2["employedPopulation"].tolist()
    
    # 線條2
    numberOfUnemployed = data2["numberOfUnemployed"].tolist()
    
    # # # 線條3
    # domesticInvestment = data2["domesticInvestment"].tolist()
    
    # # 線條4 - 人均收入
    # perCapitaIncome = data1['國民所得毛額GNI(名目值，百萬元)'].tolist()
    # perCapitaIncome = [data.replace(",", "") for data in perCapitaIncome]
    
    data2 = data2.to_dict(orient="records")
    # print(type(data2))
    context = {
        "year_xlabels" : json.dumps(year_xlabels),
        "employedPopulation_male": json.dumps(employedPopulation_male),
        "numberOfUnemployed": json.dumps(numberOfUnemployed),
    #     "domesticInvestment": json.dumps(domesticInvestment),
    #     "perCapitaIncome": json.dumps(perCapitaIncome),
    #     "data1": data1.to_dict(orient="records"),
        # "data2": data2.to_dict(orient="records"),
        "data2": data2
        }
    return render(request, "employment.html", {"context": context})
    # return render(request, "test.html", {"context": context})
    # return HttpResponse("K")











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
    csv_path = os.path.join(settings.BASE_DIR, 'static', 'csv/basicConsumerPriceIndex.csv')

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
    print(year_xlabels)
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
    
    data = data.to_dict(orient = "records")
    print(type(data))
    context = {
        "year_xlabels" : json.dumps(year_xlabels),
        "food": json.dumps(food),
        "clothing": json.dumps(clothing),
        "transportationAndCommunications": json.dumps(transportationAndCommunications),
        "medicineAndHealth": json.dumps(medicineAndHealth),
        "educationAndEntertainment": json.dumps(educationAndEntertainment),
        "miscellaneouss": json.dumps(miscellaneouss),
        "data": data
        }
    return render(request, "cpi.html", context)


# 消費與儲蓄
def consumptionandsaving(request):
    csv_path1 = os.path.join(settings.BASE_DIR, 'static', 'csv/NationalIncomeStatistics(perCapitaIncome).csv')
    csv_path2 = os.path.join(settings.BASE_DIR, 'static', 'csv/nationalIncome_SavingsAndInvestment.csv')

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
    
    # 線條1
    nationalConsumption = data2["nationalConsumption"].tolist()
    
    # 線條2
    nationalSavings = data2["nationalSavings"].tolist()
    
    # 線條3
    domesticInvestment = data2["domesticInvestment"].tolist()
    
    # 線條4
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


# 人力資源
def humanResources(request):
    csv_path = os.path.join(settings.BASE_DIR, 'static', 'csv/人力資源主要指標.csv')
    

    # 读取 CSV 文件
    data = pd.read_csv(csv_path, encoding="big5", skiprows=2)

    # data1=data1[:-3]
    # data2=data2[:-6]

    data = data.rename(columns={"統計期": "year",
                                "總人口數(千人)-合計 ": "total_population",
                                "勞動力(千人)-合計 ": "Laborforce_total",
                                "勞動力(千人)-男 ": "Laborforce_male",
                                "勞動力(千人)-女 ":"Laborforce_female",
                                "就業人數(千人)-合計 ": "employedpopulation_total",                                
                                "就業人數(千人)-男 ": "employedpopulation_male",
                                "就業人數(千人)-女 ": "employedpopulation_female",
                                "失業人數(千人)-合計 ": "Numberofunemployed_total",
                                "勞動力參與率(%)-合計 ":"laborforceparticipationrate_total",
                                "勞動力參與率(%)-男 ": "laborforceparticipationrate_male",                                
                                "勞動力參與率(%)-女 ": "laborforceparticipationrate_female",
                                "就業人口占總人口數(%)-合計 ":"EmployedpopulationAsAShareoftotalpopulation",
                                "失業率(%)-合計": "unemploymentrate_total",})
    
    year_xlabels = data['year'].tolist()

    
    # 就業人數
    employedpopulation_total = data["employedpopulation_total"].tolist()
    
    # 失業人數
    Numberofunemployed_total = data["Numberofunemployed_total"].tolist()
    
    # # 線條3
    # domesticInvestment = data2["domesticInvestment"].tolist()
    
    # # 線條4
    # perCapitaIncome = data1['國民所得毛額GNI(名目值，百萬元)'].tolist()
    # perCapitaIncome = [data.replace(",", "") for data in perCapitaIncome]
    
    
    context = {
        "year_xlabels" : json.dumps(year_xlabels),
        "employedpopulation_total": json.dumps(employedpopulation_total),
        "Numberofunemployed_total": json.dumps(Numberofunemployed_total),
        "data": data.to_dict(orient="records"),
        }
    print(context["employedpopulation_total"])
    return render(request, "humanResources.html", {"context": context})

def test_csv(request):
    
    import json
    
    # 生成数据
    employment_data = {
        "industries": ["製造業", "批發及零售業", "農、林、漁、牧業", "營造業", "住宿及餐飲業", "教育服務業", "運輸及倉儲業", "醫療保健及社會工作服務業", "其他服務業"],
        "values": [5000, 6000, 4000, 3000, 3500, 2000, 2500, 4500, 2800]
    }
    
    # 将数据以 JSON 格式写入到 HTML 模板中
    with open('test.html', 'r') as file:
        html_template = file.read()
    
    html_template = html_template.replace("'employmentData'", json.dumps(employment_data))
    
    # 将生成的 HTML 页面写入到文件中
    with open('output.html', 'w') as file:
        file.write(html_template)

    return render(request, "test.html", locals())
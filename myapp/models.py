from django.db import models

# Create your models here.
class National_Data(models.Model):
    year = models.CharField(max_length=10)
    population = models.CharField(max_length=100)
    populationGrowth_annualGrowthRate = models.CharField(max_length=100)
    AverageExchange_rate = models.CharField(max_length=100)
    EconomicGrowth_annualGrowthRate = models.CharField(max_length=100)
    Domestic_Grossproduction_GDP_nominalValue_millionYuan = models.CharField(max_length=100)
    Domestic_Grossproduction_GDP_annualGrowthRate = models.CharField(max_length=100)
    AveragePersonalGDP = models.CharField(max_length=100)
    AveragePersonalGDP_rate = models.CharField(max_length=100)
    GrossNationalIncomeGNI_nominalValue_millionYuan = models.CharField(max_length=100)
    GrossNationalIncomeGNI_annualGrowthRate = models.CharField(max_length=100)
    AveragePersonalGNI_nominalValue_millionYuan = models.CharField(max_length=100)
    AveragePersonalGNI_rate = models.CharField(max_length=100)
    NationalIncome_nominalValue_millionYuan = models.CharField(max_length=100)
    NationalIncome_annualGrowthRate = models.CharField(max_length=100)
    AverageIncomePerson_nominalValue_millionYuan = models.CharField(max_length=100)
    AverageIncomePerson_annualGrowthRate = models.CharField(max_length=100)
    
    class Meta:
        db_table = "national_data"
    
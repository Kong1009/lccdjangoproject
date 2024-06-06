import pandas as pd
from django.core.management.base import BaseCommand
from myapp.models import National_Data

class Command(BaseCommand):
    help = 'Import CSV data into the National_Data model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        
        # 读取 CSV 文件并创建 DataFrame
        data = pd.read_csv(csv_file)
        
        # 将数据写入数据库表
        for index, row in data.iterrows():
            National_Data.objects.create(
                year=row['統計期'],
                population=row['期中人口(人)'],
                populationGrowth_annualGrowthRate=row['1.年增率(%)'],
                AverageExchange_rate=row['平均匯率(元/美元)'],
                EconomicGrowth_annualGrowthRate=row['經濟成長率(%)'],
                Domestic_Grossproduction_GDP_nominalValue_millionYuan=row['國內生產毛額GDP(名目值，百萬元)'],
                Domestic_Grossproduction_GDP_annualGrowthRate=row['國內生產毛額GDP(名目值，百萬元)'],
                AveragePersonalGDP=row['2.年增率(%)'],
                AveragePersonalGDP_rate=row['平均每人GDP(名目值，元)'],
                GrossNationalIncomeGNI_nominalValue_millionYuan=row['3.年增率(%)'],
                GrossNationalIncomeGNI_annualGrowthRate=row['國民所得毛額GNI(名目值，百萬元)'],
                AveragePersonalGNI_nominalValue_millionYuan=row['國民所得毛額GNI(名目值，百萬元)'],
                AveragePersonalGNI_rate=row['4.年增率(%)'],
                NationalIncome_nominalValue_millionYuan=row['國民所得(名目值，百萬元)'],
                NationalIncome_annualGrowthRate=row['5.年增率(%)'],
                AverageIncomePerson_nominalValue_millionYuan=row['平均每人所得(名目值，元)'],
                AverageIncomePerson_annualGrowthRate=row['6.年增率(%)']
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully imported data from "%s"' % csv_file))

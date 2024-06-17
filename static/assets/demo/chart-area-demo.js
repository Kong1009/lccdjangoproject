// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';


document.addEventListener('DOMContentLoaded', function () {
  var chartType = document.getElementById('chart').dataset.chartType;
  var labels = JSON.parse(document.getElementById('year_xlabels').textContent);

  // 判斷是哪張圖表來找資料
  if (chartType === "cpi"){
    var food = JSON.parse(document.getElementById('food').textContent);
    var clothing = JSON.parse(document.getElementById('clothing').textContent);
    var transportationAndCommunications = JSON.parse(document.getElementById('transportationAndCommunications').textContent);
    var medicineAndHealth = JSON.parse(document.getElementById('medicineAndHealth').textContent);
    var educationAndEntertainment = JSON.parse(document.getElementById('educationAndEntertainment').textContent);
    var miscellaneouss = JSON.parse(document.getElementById('miscellaneouss').textContent);
  } 
  else if (chartType === "consumptionandsaving"){

    // 获取嵌入在 HTML 中的 JSON 数据
    var nationalConsumption_values = JSON.parse(document.getElementById('nationalConsumption').textContent);
    var nationalSavings_values = JSON.parse(document.getElementById('nationalSavings').textContent);
    var domesticInvestment_values = JSON.parse(document.getElementById('domesticInvestment').textContent);
    // var perCapitaIncome_values = JSON.parse(document.getElementById('perCapitaIncome').textContent);
  }
  else if (chartType === "agriculture_forestry_fishery_animalHusbandry"){
  
    // 获取嵌入在 HTML 中的 JSON 数据
    var agriculture_forestry_fishery_animalHusbandry = JSON.parse(document.getElementById('agriculture_forestry_fishery_animalHusbandry').textContent);
    var manufacturing = JSON.parse(document.getElementById('manufacturing').textContent);
    var WholesaleandRetailTrade = JSON.parse(document.getElementById('WholesaleandRetailTrade').textContent);
    var constructionIndustry = JSON.parse(document.getElementById('constructionIndustry').textContent);
    var AccommodationandCateringUndustry = JSON.parse(document.getElementById('AccommodationandCateringUndustry').textContent);
    var EducationalServiceIndustry = JSON.parse(document.getElementById('EducationalServiceIndustry').textContent);
    var TransportationandWarehousingIndustry = JSON.parse(document.getElementById('TransportationandWarehousingIndustry').textContent);
    var HealthcareAndSocialWorkServicesIndustry = JSON.parse(document.getElementById('HealthcareAndSocialWorkServicesIndustry').textContent);
    var OtherServiceindustries = JSON.parse(document.getElementById('OtherServiceindustries').textContent);
  }
  else if (chartType === "population"){      
    // 获取嵌入在 HTML 中的 JSON 数据
    var Numberofbirths = JSON.parse(document.getElementById('Numberofbirths').textContent);
    var birthRate = JSON.parse(document.getElementById('birthRate').textContent);
    var NumberofMaleBirths = JSON.parse(document.getElementById('NumberofMaleBirths').textContent);
    var NumberofFemaleBirths = JSON.parse(document.getElementById('NumberofFemaleBirths').textContent);
    var NumberofDeaths = JSON.parse(document.getElementById('NumberofDeaths').textContent);
    var mortalityRate = JSON.parse(document.getElementById('mortalityRate').textContent);    
  };




  // 判斷資料中的最大值
  if (chartType === "consumptionandsaving"){    
    var maxDataValue = Math.max(

      Math.max(...nationalConsumption_values),
      Math.max(...nationalSavings_values),
      Math.max(...domesticInvestment_values)
      
    );
  } 
  else if (chartType === "cpi"){
    var maxDataValue = Math.max(
      Math.max(...food),
      Math.max(...clothing),
      Math.max(...transportationAndCommunications),
      Math.max(...medicineAndHealth),
      Math.max(...educationAndEntertainment),
      Math.max(...miscellaneouss)
    );
  }
  else if (chartType === "agriculture_forestry_fishery_animalHusbandry"){
    var maxDataValue = Math.max(
      Math.max(...agriculture_forestry_fishery_animalHusbandry),
      Math.max(...manufacturing),
      Math.max(...WholesaleandRetailTrade),
      Math.max(...constructionIndustry),
      Math.max(...AccommodationandCateringUndustry),
      Math.max(...EducationalServiceIndustry),
      Math.max(...TransportationandWarehousingIndustry),
      Math.max(...HealthcareAndSocialWorkServicesIndustry),
      Math.max(...OtherServiceindustries)
    );
  }
  else if (chartType === "population"){
    var maxDataValue = Math.max(
      Math.max(...Numberofbirths ),
      Math.max(...birthRate),
      Math.max(...NumberofMaleBirths),
      Math.max(...NumberofFemaleBirths),
      Math.max(...NumberofDeaths),
      Math.max(...mortalityRate),
    );
  };


// 圖表資料
  var ctx = document.getElementById("myAreaChart");
  var datasets;
  if (chartType === "cpi") {
    datasets = [
        {
            label: "食品",
            lineTension: 0.5,
            backgroundColor: "rgba(2,117,216,0.2)",
            borderColor: "red",
            pointRadius: 5,
            pointBackgroundColor: "red",
            pointBorderColor: "rgba(255,255,255,0.8)",
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(2,117,216,1)",
            pointHitRadius: 50,
            pointBorderWidth: 2,
            data: food,
        },
        {
            label: "服裝",
            lineTension: 0.5,
            backgroundColor: "rgba(2,117,216,0.2)",
            borderColor: "green",
            pointRadius: 5,
            pointBackgroundColor: "green",
            pointBorderColor: "rgba(255,255,255,0.8)",
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(2,117,216,1)",
            pointHitRadius: 50,
            pointBorderWidth: 2,
            data: clothing,
        },{
          label: "交通及通訊類",
          lineTension: 0.5,
          backgroundColor: "rgba(2,117,216,0.2)",
          borderColor: "blue",
          pointRadius: 5,
          pointBackgroundColor: "blue",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(2,117,216,1)",
          pointHitRadius: 50,
          pointBorderWidth: 2,
          data: transportationAndCommunications,
      },
      {
            label: "醫藥保健類",
            lineTension: 0.5,
            backgroundColor: "rgba(2,117,216,0.2)",
            borderColor: "purple",
            pointRadius: 5,
            pointBackgroundColor: "purple",
            pointBorderColor: "rgba(255,255,255,0.8)",
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(2,117,216,1)",
            pointHitRadius: 50,
            pointBorderWidth: 2,
            data: medicineAndHealth,
        },
        {
          label: "教養娛樂類",
          lineTension: 0.5,
          backgroundColor: "rgba(2,117,216,0.2)",
          borderColor: "orange",
          pointRadius: 5,
          pointBackgroundColor: "orange",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(2,117,216,1)",
          pointHitRadius: 50,
          pointBorderWidth: 2,
          data: educationAndEntertainment,
      },
      {
        label: "雜項",
        lineTension: 0.5,
        backgroundColor: "rgba(2,117,216,0.2)",
        borderColor: "yellow",
        pointRadius: 5,
        pointBackgroundColor: "yellow",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,117,216,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: miscellaneouss,
    }
        // 其他資料集...
    ];
  } 
  else if (chartType === "consumptionandsaving") {
      datasets = [
          {
              label: "國民消費",
              lineTension: 0.5,
              backgroundColor: "rgba(2,117,216,0.2)",
              borderColor: "red",
              pointRadius: 5,
              pointBackgroundColor: "red",
              pointBorderColor: "rgba(255,255,255,0.8)",
              pointHoverRadius: 5,
              pointHoverBackgroundColor: "rgba(2,117,216,1)",
              pointHitRadius: 50,
              pointBorderWidth: 2,
              data: nationalConsumption_values,
          },
          {
              label: "國民儲蓄毛額",
              lineTension: 0.5,
              backgroundColor: "rgba(2,117,216,0.2)",
              borderColor: "green",
              pointRadius: 5,
              pointBackgroundColor: "green",
              pointBorderColor: "rgba(255,255,255,0.8)",
              pointHoverRadius: 5,
              pointHoverBackgroundColor: "rgba(2,117,216,1)",
              pointHitRadius: 50,
              pointBorderWidth: 2,
              data: nationalSavings_values,
          },
          {
            label: "國民儲蓄",
            lineTension: 0.5,
            backgroundColor: "rgba(2,117,216,0.2)",
            borderColor: "blue",
            pointRadius: 5,
            pointBackgroundColor: "blue",
            pointBorderColor: "rgba(255,255,255,0.8)",
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(2,117,216,1)",
            pointHitRadius: 50,
            pointBorderWidth: 2,
            data: domesticInvestment_values,
        },
      ];
  }
  else if (chartType === "population") {
    datasets = [
      {
          label: "死亡總數",
          type: "line",
          lineTension: 0.5,
          backgroundColor: "rgba(2,117,216,0.2)",
          borderColor: "red",
          pointRadius: 5,
          pointBackgroundColor: "red",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(2,117,216,1)",
          pointHitRadius: 50,
          pointBorderWidth: 2,
          data: NumberofDeaths,
      }

    ];
  }
  else if (chartType === "agriculture_forestry_fishery_animalHusbandry") {
    datasets = [
        {
            label: "農、林、漁、牧業",
            lineTension: 0.5,
            // backgroundColor: "rgba(2,117,216,0.2)",
            borderColor: "red",
            pointRadius: 5,
            pointBackgroundColor: "red",
            pointBorderColor: "rgba(255,255,255,0.8)",
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(2,117,216,1)",
            pointHitRadius: 50,
            pointBorderWidth: 2,
            data: agriculture_forestry_fishery_animalHusbandry,
        },
        {
            label: "製造業",
            lineTension: 0.5,
            backgroundColor: "rgba(2,117,216,0)",
            borderColor: "green",
            pointRadius: 5,
            pointBackgroundColor: "green",
            pointBorderColor: "rgba(255,255,255,0.8)",
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(2,117,216,1)",
            pointHitRadius: 50,
            pointBorderWidth: 2,
            data: manufacturing,
        },
        {
            label: "批發及零售業",
            lineTension: 0.5,
            backgroundColor: "rgba(2,117,216,0.1)",
            borderColor: "yellow",
            pointRadius: 5,
            pointBackgroundColor: "yellow",
            pointBorderColor: "rgba(255,255,255,0.8)",
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(2,117,216,1)",
            pointHitRadius: 50,
            pointBorderWidth: 2,
            data: WholesaleandRetailTrade,
        },
        {
          label: "營造業",
          lineTension: 0.5,
          backgroundColor: "rgba(2,117,216,0)",
          borderColor: "blue",
          pointRadius: 5,
          pointBackgroundColor: "blue",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(2,117,216,1)",
          pointHitRadius: 50,
          pointBorderWidth: 2,
          data: constructionIndustry,
      },
        {
          label: "住宿及餐飲業",
          lineTension: 0.5,
          backgroundColor: "rgba(2,117,216,0)",
          borderColor: "Purple",
          pointRadius: 5,
          pointBackgroundColor: "Purple",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(2,117,216,1)",
          pointHitRadius: 50,
          pointBorderWidth: 2,
          data: AccommodationandCateringUndustry,
      },
        {
          label: "教育服務業",
          lineTension: 0.5,
          backgroundColor: "rgba(2,117,216,0)",
          borderColor: "orange",
          pointRadius: 5,
          pointBackgroundColor: "orange",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(2,117,216,1)",
          pointHitRadius: 50,
          pointBorderWidth: 2,
          data: EducationalServiceIndustry,
      },
        {
          label: "運輸及倉儲業",
          lineTension: 0.5,
          backgroundColor: "rgba(2,117,216,0)",
          borderColor: "gray",
          pointRadius: 5,
          pointBackgroundColor: "gray",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(2,117,216,1)",
          pointHitRadius: 50,
          pointBorderWidth: 2,
          data: TransportationandWarehousingIndustry,
      },
        {
          label: "醫療保健及社會工作服務業",
          lineTension: 0.5,
          backgroundColor: "rgba(2,117,216,0)",
          borderColor: "gold",
          pointRadius: 5,
          pointBackgroundColor: "gold",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(2,117,216,1)",
          pointHitRadius: 50,
          pointBorderWidth: 2,
          data: HealthcareAndSocialWorkServicesIndustry,
      },
        {
          label: "其他服務業",
          lineTension: 0.5,
          backgroundColor: "rgba(2,117,216,0)",
          borderColor: "black",
          pointRadius: 5,
          pointBackgroundColor: "black",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(2,117,216,1)",
          pointHitRadius: 50,
          pointBorderWidth: 2,
          data: OtherServiceindustries,
      },
        // 其他資料集...
    ];
  }


  var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: datasets
    },
    options: {
      scales: {
        xAxes: [{
          time: {
            unit: 'date'
          },
          gridLines: {
            display: false
          },
          ticks: {
            maxTicksLimit: 15
          }
        }],
        yAxes: [{
          ticks: {
            min: 0,
            max: maxDataValue,
            maxTicksLimit: 10
          },
          gridLines: {
            color: "rgba(0, 0, 0, .125)",
          }
        }],
      },
      legend: {
        
        display: true
      },
      responsive: true,
      hover: {
        mode: 'nearest',
        intersect: false
      },
      tooltips: {
        mode: 'nearest',
        intersect: false
      }

    }
  });
});
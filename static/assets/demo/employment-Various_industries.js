// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
document.addEventListener('DOMContentLoaded', function () {
  var ctx = document.getElementById("myAreaChart");
  var labels = JSON.parse(document.getElementById('year_xlabels').textContent);


  var agriculture_forestry_fishery_animalHusbandry = JSON.parse(document.getElementById('agriculture_forestry_fishery_animalHusbandry').textContent);
  var manufacturing = JSON.parse(document.getElementById('manufacturing').textContent);
  var WholesaleandRetailTrade = JSON.parse(document.getElementById('WholesaleandRetailTrade').textContent);
  var constructionIndustry = JSON.parse(document.getElementById('constructionIndustry').textContent);
  var AccommodationandCateringUndustry = JSON.parse(document.getElementById('AccommodationandCateringUndustry').textContent);
  var EducationalServiceIndustry = JSON.parse(document.getElementById('EducationalServiceIndustry').textContent);
  var TransportationandWarehousingIndustry = JSON.parse(document.getElementById('TransportationandWarehousingIndustry').textContent);
  var HealthcareAndSocialWorkServicesIndustry = JSON.parse(document.getElementById('HealthcareAndSocialWorkServicesIndustry').textContent);
  var OtherServiceindustries = JSON.parse(document.getElementById('OtherServiceindustries').textContent);
  
  var datasets;
  datasets = [
    {
        label: "農、林、漁、牧業",
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
        data: agriculture_forestry_fishery_animalHusbandry,
    },
    {
        label: "製造業",
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
        data: manufacturing,
    },{
      label: "批發及零售業",
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
      data: WholesaleandRetailTrade,
  },
  {
        label: "營造業",
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
        data: constructionIndustry,
    },
    {
      label: "住宿及餐飲業",
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
      data: AccommodationandCateringUndustry,
  },
  {
    label: "教育服務業",
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
    data: EducationalServiceIndustry,
  }
    // 其他資料集...
  ];
  var maxDataValue = Math.max(

    Math.max(...agriculture_forestry_fishery_animalHusbandry)

    
  );


  var myLineChart = new Chart(ctx, {

    type: 'line',
    data: {
      labels: labels,
      datasets: {
        label: labels,      
        data: datasets,
      },
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
            maxTicksLimit: 7
          }
        }],
        yAxes: [{
          ticks: {
            min: 0,
            max: maxDataValue,
            maxTicksLimit: 5
          },
          gridLines: {
            color: "rgba(0, 0, 0, .125)",
          }
        }],
      },
      legend: {
        display: false
      }
    }
  });
});
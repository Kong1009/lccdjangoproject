// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
document.addEventListener('DOMContentLoaded', function () {
  // 获取嵌入在 HTML 中的 JSON 数据
  var labels = JSON.parse(document.getElementById('year_xlabels').textContent);
  var Numberofbirths = JSON.parse(document.getElementById('Numberofbirths').textContent);
  var birthRate = JSON.parse(document.getElementById('birthRate').textContent);
  var NumberofMaleBirths = JSON.parse(document.getElementById('NumberofMaleBirths').textContent);
  var NumberofFemaleBirths = JSON.parse(document.getElementById('NumberofFemaleBirths').textContent);
  var NumberofDeaths = JSON.parse(document.getElementById('NumberofDeaths').textContent);
  var mortalityRate = JSON.parse(document.getElementById('mortalityRate').textContent);   

  var maxDataValue = Math.max(

    Math.max(...NumberofFemaleBirths),
    Math.max(...NumberofMaleBirths),

    
  );

  var datasets;
  datasets = [
    {
        label: "男生",
        lineTension: 0.5,
        backgroundColor: "blue",
        borderColor: "blue",
        pointRadius: 5,
        pointBackgroundColor: "red",
        pointBorderColor: "blue",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,117,216,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: NumberofMaleBirths,
    },{
      label: "女生",
      lineTension: 0.5,
      backgroundColor: "red",
      borderColor: "red",
      pointRadius: 5,
      pointBackgroundColor: "red",
      pointBorderColor: "red",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,117,216,1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: NumberofFemaleBirths,
  }
  ]

  var ctx = document.getElementById("myBarChart");
  var myLineChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: datasets
    },
    options: {
      scales: {
        xAxes: [{
          time: {
            unit: 'month'
          },
          gridLines: {
            display: false
          },
          ticks: {
            maxTicksLimit: 6
          }
        }],
        yAxes: [{
          ticks: {
            min: 0,
            max: maxDataValue,
            maxTicksLimit: 5
          },
          gridLines: {
            display: true
          }
        }],
      },
      legend: {
        display: false
      },
      responsive: true,

    }
  });
});

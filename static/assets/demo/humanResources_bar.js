// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
document.addEventListener('DOMContentLoaded', function () {
  // 获取嵌入在 HTML 中的 JSON 数据
  var labels = JSON.parse(document.getElementById('year_xlabels').textContent);
  var employedpopulation_total = JSON.parse(document.getElementById('employedpopulation_total').textContent);
  var Numberofunemployed_total = JSON.parse(document.getElementById('Numberofunemployed_total').textContent);

    // 調試輸出
    console.log('Labels:', labels);
    console.log('Employed Population Total:', employedpopulation_total);
    console.log('Number of Unemployed Total:', Numberofunemployed_total);
  var maxDataValue = Math.max(

    Math.max(...employedpopulation_total),
    Math.max(...Numberofunemployed_total),

    
  );

  var datasets;
  datasets = [
    {
        label: "就業人數",
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
        data: employedpopulation_total,
    },{
      label: "失業人數",
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
      data: Numberofunemployed_total,
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

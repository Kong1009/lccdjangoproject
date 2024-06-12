// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart
document.addEventListener('DOMContentLoaded', function () {
  // 获取嵌入在 HTML 中的 JSON 数据
  var labels = JSON.parse(document.getElementById('year_xlabels').textContent);
  var nationalConsumption = JSON.parse(document.getElementById('nationalConsumption').textContent);
  var numberOfUnemployed = JSON.parse(document.getElementById('numberOfUnemployed').textContent);

  var ctx = document.getElementById("myBarChart");
  var myLineChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: "平均每人所得(年)",
        backgroundColor: "rgba(2,117,216,1)",
        borderColor: "rgba(2,117,216,1)",
        data: nationalConsumption,
      }],
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
            max: 15000,
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

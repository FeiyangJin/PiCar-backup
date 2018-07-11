var ctx = document.getElementById("myChart");
var labelForChart = ["Jan","Feb","Mar","Apr","May"];
var dataForChart = [30,40,48,62]
dataForChart.push(15)

var timeLabel = []
var imuAXdata = []
var imuAYdata = []

var updateDataChart = function(optionString){
  if(optionString === "add"){
    var allRowData3 = csvData.data[time]
    var dataTime = allRowData3[0]
    var imuAX = allRowData3[2]
    var imuAY = allRowData3[3]
    var dataSet = [imuAX,imuAY]
    addData(chart,dataTime,dataSet);
  }
  else if(optionString === "remove"){
    removeData(chart);
  }
  else if(optionString === "clear"){
    console.log("we want to clear the chart")
    var i = 1;
    var length = chart.data.labels.length
    while(i < length){
      removeData(chart);
      i++;
    }
  }

}

var chart = new Chart(ctx,{
  type: 'line',
  data: {
    labels:[],
    datasets: [{
      label: 'imu accelaration x',
      borderColor:"red",
      data: [],
      borderWidth:1
    },
    {
      label: 'imu accelaration y',
      borderColor:"blue",
      data: [],
      borderWidth:1
    }]
  },
  options:{
    responsive:false,
  }

})

// var dataArray = [0,-5]
// var count = 0
// chart.data.labels.push("May");
// chart.data.datasets.forEach((dataset) => {
//     dataset.data.push(dataArray[count]);
//     count++;
// });
// count = 0;
// chart.update();


function addData(chart, label, dataSet) {
    chart.data.labels.push(label);
    var count = 0;
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(dataSet[count]);
        count++;
    });
    chart.update();
}

function removeData(chart) {
    chart.data.labels.pop();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.pop();
    });
    chart.update();
}

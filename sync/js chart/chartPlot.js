var ctx = document.getElementById("myChart");
var maxDataSets = 50;


//update the chart based on option
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


//make the initial blank chart
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

//add data to the front of graph
function unshiftData(chart,label,dataSet){
    chart.data.labels.unshift(label);
    var count = 0
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(dataSet[count]);
        count++;
    });
    chart.update();
}

//add data based to the end of graph
function addData(chart, label, dataSet) {
    chart.data.labels.push(label);
    var count = 0;
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(dataSet[count]);
        count++;
    });
    if(chart.data.labels.length > maxDataSets){
      shiftData(chart);
    }
    chart.update();
}


//remove first data
function shiftData(chart){
  chart.data.labels.shift();
  chart.data.datasets.forEach((dataset) => {
      dataset.data.shift();
  });
  chart.update();
}


//remove last data
function removeData(chart) {
    chart.data.labels.pop();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.pop();
    });
    if(chart.data.labels.length < maxDataSets){
      if(time >= maxDataSets){
        var allRowData4 = csvData.data[time - maxDataSets]
        var dataTime = allRowData4[0]
        var imuAX = allRowData4[2]
        var imuAY = allRowData4[3]
        var dataSet = [imuAX,imuAY]
        unshiftData(chart,dataTime,dataSet);
      }
    }
    chart.update();
}

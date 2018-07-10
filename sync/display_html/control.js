var time = 0;
var csvData;
var photoPos = 8;
var AllphotoPath = "/Users/kinfeiyang/Desktop/ok/camera/";

imageDiv = document.getElementById("image_div");

var increaseTime = function(){
  time = time + 1;
  console.log(time)
  if(time >= csvData.data.length){
    alert("no more afterwards data")
    time = time - 1
    console.log(time)
  }
  else{
    updateData();
    updateImage();
  }

}
document.getElementById('next_button').addEventListener('click',increaseTime)

var decreaseTime = function(){
  time = time - 1;
  console.log(time);
  if (time < 0){
    alert("no more previous data")
    time = time + 1
    console.log(time)
  }
  else{
    updateData();
    updateImage();
  }

}
document.getElementById("prev_button").addEventListener('click',decreaseTime)

//parse csv file
function loadFileAsText(){
  var fileToLoad = document.getElementById("fileToLoad").files[0];
  Papa.parse(fileToLoad, {
    delimiter: ",",
    header: false,
  	complete: function(results) {
      csvData = results;
  		console.log(results);
      document.getElementById("move_button").hidden = false
      updateData();
      updateImage();
  	}
  });
}

//update data
function updateData(){
  allRowData = csvData.data[time]
  dataTime = allRowData[0]
  Lidar = allRowData[1]
  imuAX = allRowData[2]
  imuAY = allRowData[3]
  imuAZ = allRowData[4]
  imuGX = allRowData[5]
  imuGY = allRowData[6]
  imuGZ = allRowData[7]
  document.getElementById('time_data').innerHTML = "<h3>" + "Time:  " + dataTime + "<h3> <br>";
  document.getElementById('lidar_data').innerHTML = "<h3>" + "Lidar distance:  " + Lidar + "<h3> <br>";
  document.getElementById('imu_data').innerHTML = "<h3>" + "IMU data:  " + imuAX + ",  " + imuAY + ",  "
  + imuAZ + ",  " + imuGX + ",  " + imuGY + ",  " + imuGZ + "<h3>";

}

//update image
function updateImage(){
  allRowData2 = csvData.data[time]
  filePath = AllphotoPath + allRowData2[photoPos]
  console.log(filePath)
  imageDiv.innerHTML = ""
  var image = document.createElement("img");
  image.setAttribute('src',filePath)
  image.setAttribute('width','500')
  imageDiv.appendChild(image);
}

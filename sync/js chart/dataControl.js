var time = 0;
var csvData;
var photoPos = 11;
var AllphotoPath = "/Users/kinfeiyang/Desktop/710/camera/";
var PlayTimer
imageDiv = document.getElementById("image_div");


var jump_first = function(){
  time = 0
  updateData();
  updateImage();
  updateDataChart("clear");
}
document.getElementById("first_button").addEventListener('click',jump_first)


var stopAutoPlay = function(){
  clearInterval(PlayTimer)
  console.log("you stop the auto play")
  document.getElementById("autoPlay_button").hidden = false
  document.getElementById("autoPlay_frequency").hidden = false
  document.getElementById("autoPlay_stop").hidden = true
}
document.getElementById('autoPlay_stop').addEventListener('click',stopAutoPlay)


var autoPlayTimer = function(){
  if(time == csvData.data.length - 1 || time > (csvData.data.length - 1)){
    clearInterval(PlayTimer)
    document.getElementById("autoPlay_button").hidden = false
    document.getElementById("autoPlay_frequency").hidden = false
    document.getElementById("autoPlay_stop").hidden = true
  }
  else{
    document.getElementById('next_button').click()
  }

}


var autoPlay = function(){
    var frequency = 1000
    if(document.getElementById("autoPlay_frequency").value){
      frequency = document.getElementById("autoPlay_frequency").value * 1000;
    }

    PlayTimer = setInterval(autoPlayTimer,frequency)
    //hide autoplay button, show stop button
    document.getElementById("autoPlay_button").hidden = true
    document.getElementById("autoPlay_frequency").hidden = true
    document.getElementById("autoPlay_stop").hidden = false
}
document.getElementById("autoPlay_button").addEventListener('click',autoPlay)


var increaseTime = function(){
  time = time + 1;
  console.log(time)
  if(time == csvData.data.length || time > csvData.data.length){
    alert("no more afterwards data")
    clearInterval(PlayTimer)
    time = time - 1
    console.log(time)
  }
  else{
    updateData();
    updateImage();
    updateDataChart("add");
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
    updateDataChart("remove");
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
  		//console.log(results);
      document.getElementById("move_button").hidden = false
      updateData();
      updateImage();
      updateDataChart("add");
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
  document.getElementById('time_data').innerHTML = "<h3>" + "Time:  " + dataTime + "</h3> <br>";
  document.getElementById('lidar_data').innerHTML = "<h3>" + "Lidar distance:  " + Lidar + "</h3> <br>";
  document.getElementById('imu_data').innerHTML = "<h3>" + "IMU data:  " + imuAX + ",  " + imuAY + ",  "
  + imuAZ + ",  " + imuGX + ",  " + imuGY + ",  " + imuGZ + "</h3>";

}


//update image
function updateImage(){
  allRowData2 = csvData.data[time]
  filePath = AllphotoPath + allRowData2[photoPos]
  //console.log(filePath)
  if(!(allRowData2[photoPos] === undefined)){
    imageDiv.innerHTML = ""
    var image = document.createElement("img");
    image.setAttribute('src',filePath)
    image.setAttribute('width','400')
    image.setAttribute('height','400')
    imageDiv.appendChild(image);
  }

}

#include <Wire.h>
#define SLAVE_ADDRESS 0x04

byte inputByte = 0;
byte byteArray[100] = {1,2,3,4,5,6,7,8,9,10};
double outputByte = 0;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); // start serial for output
  

  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  
  //set i2c speed
  //Wire.setClock(400000L);
  
  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.println("Ready!");
}

void loop() {
  delay(500);
  if(Serial.available()){
      byte input = Serial.read();
      if(input == 51){
        Serial.print("outputByte is:");
        Serial.println(outputByte);
        outputByte = 0;
      }
      
  }
}

// callback for received data
void receiveData(int byteCount){
  inputByte = Wire.read();
}


// callback for sending data
void sendData(){
  Wire.write("9");
  //Wire.write("15");
  outputByte ++;
  //Serial.println(outputByte);
  //for(int  i=0; i<100; i++){
  //  Wire.write(i);
  //}
}

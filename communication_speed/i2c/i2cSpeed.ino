/*
Author: Feiyang Jin
Email: feiyang.jin@wustl.edu
Organization: Washington University in St. Louis
Date: July 2018
*/

#include <Wire.h>
#define SLAVE_ADDRESS 0x04

byte inputByte = 0;
double outputByte = 0;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600); // start serial for output


  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);

  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.println("Ready!");
}

void loop() {
  //in serial monitor, type in 3 to read count
  //3 in ascii is 51
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
  Wire.write(9);
  outputByte ++;
}

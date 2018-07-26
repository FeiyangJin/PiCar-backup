/*
Author: Feiyang Jin
Email: feiyang.jin@wustl.edu
Organization: Washington University in St. Louis
Date: July 2018
*/

#include <Wire.h>
#define SLAVE_ADDRESS 0x04
int data = 3;
int state = 0;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);

  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);

  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  Serial.println("Ready!");
}

void loop() {
  delay(100);
}

// callback for received data
void receiveData(int byteCount){
  while(Wire.available()) {
    outputdata = Wire.read();
    Serial.print("data received: ");
    Serial.println(outputdata);
    if (outputdata == 1){
      if (state == 0){
        digitalWrite(13, HIGH); // set the LED on
        state = 1;
      }
      else{
        digitalWrite(13, LOW); // set the LED off
        state = 0;
      }
    }
  }
}

// callback for sending data
void sendData(){
  Serial.print("data sent:");
  Serial.println(data);
  Wire.write(data);

}

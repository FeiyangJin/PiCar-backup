float data = 3.14159;

void setup(){
Serial.begin(9600);
}

void loop(){
  //Serial.println("hello");
  sendFloat();
  delay(2000);
}

void sendFloat(){
  volatile unsigned long rawBits;
  rawBits =  *(unsigned long *) &data;
  //first write float header
  Serial.write("#");
  Serial.write(rawBits >> 24 & 0xff);
  Serial.write(rawBits >> 16 & 0xff);
  Serial.write(rawBits >> 8 & 0xff);
  Serial.write(rawBits & 0xff);
}

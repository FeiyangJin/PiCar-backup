int inputCount = 0;
int CountInTenK = 0;

void setup(){
Serial.begin(3000000);
}

void loop(){
//Serial.println("Hi");
if(Serial.available() > 0){
  byte input = Serial.read();
  if(input == 51){
    Serial.print("input count is:");
    Serial.println(inputCount);
    Serial.print("Count in ten k is:");
    Serial.println(CountInTenK);
    inputCount = 0;
  }
  else if (input != 0){
    //int Int = input;
    //char Char = input;
    //Serial.print("we received:");
    //Serial.println(Char);
    inputCount ++;
    if(inputCount > 10000 || inputCount == 10000){
       CountInTenK ++;
       inputCount = 0;
    }
  }
}
}

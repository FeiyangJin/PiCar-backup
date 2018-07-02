#include <SPI.h>

byte inputByte = 99;
byte outputByte = 7;
int outputCount = 0;

void setup (void)
{
  Serial.begin(9600);
  pinMode(MISO, OUTPUT);
  SPI.setClockDivider(SPI_CLOCK_DIV2);
  SPCR |= _BV(SPE);
  SPDR = 9;
  Serial.println("Ready");
}

void loop (void)
{
  if(Serial.available()){
      byte input = Serial.read();
      //51 is int 3
      if(input == 51){
        Serial.print("outputCount is:");
        Serial.println(outputCount);
        outputCount = 0;
      }
      
  }
  
  //if there is something to read
  if((SPSR & (1 << SPIF)) != 0)
  {
    inputByte = SPDR;
    SPDR = outputByte;
    outputCount ++;
    //Serial.println(inputByte);
  }

}


#include <SPI.h>
//Notice: SPI.h is used for arduino as master
//As a result, we cannot set spi speed using the funcion in library
// Written by Feiyang Jin
// July 2018

int CountInTenK = 0;
int inputCount = 0;
void setup (void)
{
  Serial.begin (115200);   // debugging
  // have to send on master in, *slave out*
  pinMode(MISO, OUTPUT);

  // turn on SPI in slave mode
  SPCR |= _BV(SPE);
  //SPI.setClockDivider(SPI_CLOCK_DIV2);

  // now turn on interrupts
  SPI.attachInterrupt();
  Serial.println("Ready");
}


// SPI interrupt routine
ISR (SPI_STC_vect)
{
SPDR = 3;
//byte c = SPDR;
//Serial.println(c);

inputCount ++;
if(inputCount > 10000 || inputCount == 10000){
  CountInTenK ++;
  inputCount = 0;
}
//Serial.print("we receive:");
//Serial.println(c);
}  // end of interrupt routine SPI_STC_vect

// main loop - wait for flag set in interrupt routine
void loop (void)
{
  //in serial monitor, type in 3 to read count
    if(Serial.available()){
      byte input = Serial.read();
      if(input == 51){
        Serial.print("input count is:");
        Serial.println(inputCount);
        Serial.print("Count in ten k is:");
        Serial.println(CountInTenK);
        inputCount = 0;
      }

  }

}  // end of loop

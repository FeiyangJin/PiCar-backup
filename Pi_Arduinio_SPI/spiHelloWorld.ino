/*************************************************************
 SPI_Hello_Raspi
   Configures Arduino as an SPI slave and demonstrates
   bidirectional communication with an Raspberry Pi SPI master
****************************************************************/

#include <SPI.h>

byte c = 0;

/***************************************************************  
 Setup SPI in slave mode (1) define MISO pin as output (2) set
 enable bit of the SPI configuration register 
****************************************************************/ 
                    
void setup (void)
{
  Serial.begin(9600);
  pinMode(MISO, OUTPUT);
  SPCR |= _BV(SPE);
  
}  

/***************************************************************  
 Loop until the SPI End of Transmission Flag (SPIF) is set
 indicating a byte has been received.  When a byte is
 received, load the byte,print it, and put 0x08 into SPDR for pi
 to read
****************************************************************/

void loop (void)
{

  if((SPSR & (1 << SPIF)) != 0)
  {
    //arduino should receive 3 and 4
    //and send 8 to pi
    c = SPDR;
    Serial.print("we received: ");
    Serial.println(c);
    SPDR = 8;
  }
  
}

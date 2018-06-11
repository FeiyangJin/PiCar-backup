/*************************************************************
 SPI_Hello_Raspi
   Configures an ATMEGA as an SPI slave and demonstrates
   bidirectional communication with an Raspberry Pi SPI master
   by repeatedly sending the text "Hello Raspi"
****************************************************************/


/***************************************************************
 Global Variables
  -hello[] is an array to hold the data to be transmitted
  -marker is used as a pointer in traversing data arrays
/***************************************************************/
#include <SPI.h>

unsigned char hello[] = {'H','e','l','l','o',' ',
                         'R','a','s','p','i','!','\n'};
byte marker = 0;
 
char buf[100];
volatile byte pos;
volatile boolean process_it;
volatile boolean sig;

byte c = 0;
int i = 0;
/***************************************************************  
 Setup SPI in slave mode (1) define MISO pin as output (2) set
 enable bit of the SPI configuration register 
****************************************************************/ 
                    
void setup (void)
{
  Serial.begin(9600);
  pinMode(MISO, OUTPUT);
  SPCR |= _BV(SPE);
  
  pos = 0;
  process_it = false;
  sig = false;
  
}  

//ISR (SPI_STC_vect){
//byte c = SPDR;
//
//if((SPSR & (1 << SPIF)) != 0)
//  {
//    //byte c = SPDR;
//    //Serial.println(c);
//    SPDR = hello[marker];
//    marker++;
//   
//    if(marker > sizeof(hello))
//    {
//      marker = 0;
//    }  
//    
//  if(pos < sizeof buf){
//    buf[pos++] = c;
//    process_it = true;
//  }
//}
//}

//void loop (void)
//{
//
//  if (process_it)
//    {
//    buf [pos] = 0;  
//    Serial.println (buf);
//    pos = 0;
//    process_it = false;
//    }
//    
//    
//}

/***************************************************************  
 Loop until the SPI End of Transmission Flag (SPIF) is set
 indicating a byte has been received.  When a byte is
 received, load the next byte in the Hello[] array into SPDR
 to be transmitted to the Raspberry Pi, and increment the marker.
 If the end of the Hell0[] array has been reached, reset
 marker to 0.
****************************************************************/

void loop (void)
{

  if((SPSR & (1 << SPIF)) != 0)
  {
    c = SPDR;
    Serial.println(c);
    //Serial.println(c);
    //SPDR = hello[marker];
    SPDR = 8;
    marker++;
   
    if(marker > sizeof(hello))
    {
      marker = 0;
    }
    
  }
  
}

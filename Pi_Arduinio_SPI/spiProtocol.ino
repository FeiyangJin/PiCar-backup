#include <SPI.h>

byte inputByte = 100;

int beginSendingFloat = 0;
int currentSendFloatByte = 1;
float data = 2.753;

int beginReadingFloat = 0;
int currentReadFloatByte = 1;

typedef union{
byte asBytes[4];
float asFloat;
} floatval;

floatval v;

void setup (void)
{
  Serial.begin(9600);
  pinMode(MISO, OUTPUT);
  SPCR |= _BV(SPE);

}

void loop (void)
{
  //if there is something to read
  if((SPSR & (1 << SPIF)) != 0)
  {
    inputByte = SPDR;
    //Serial.print("we received: ");
    //Serial.println(c);
    
    //if we receive 2, we know pi wants to read a float
    if(inputByte == 2){
      SPDR = 35;
      beginSendingFloat = 1;
    }
    else if(inputByte == 3){
      SPDR = 36;
      beginReadingFloat = 1;
    }
    else if(inputByte == 0 && beginSendingFloat){
      sendFloatByByte();
    }
    else if(beginReadingFloat){
      readFloatByByte();
    }
    
  }

}


void readFloatByByte(){
  switch(currentReadFloatByte){
    case 1:
      v.asBytes[0] = inputByte;
      currentReadFloatByte++;
      break;
    
    case 2:
      v.asBytes[1] = inputByte;
      currentReadFloatByte ++;
      break;
      
    case 3:
      v.asBytes[2] = inputByte;
      currentReadFloatByte ++;
      break;
      
    case 4:
      v.asBytes[3] = inputByte;
      currentReadFloatByte = 1;
      beginReadingFloat = 0;
      Serial.print("The float we received is:");
      Serial.println(v.asFloat,5);
      break;
  
  }
}

void sendFloatByByte(){
  volatile unsigned long rawBits;
      rawBits =  *(unsigned long *) &data;
      switch(currentSendFloatByte){
        case 1:
        SPDR = (rawBits >> 24 & 0xff);
        currentSendFloatByte ++;
        break;
        
        case 2:
        SPDR = (rawBits >> 16 & 0xff);
        currentSendFloatByte ++;
        break;
        
        case 3:
        SPDR = (rawBits >> 8 & 0xff);
        currentSendFloatByte ++;
        break;
        
        case 4:
        SPDR = (rawBits & 0xff);
        currentSendFloatByte = 1;
        beginSendingFloat = 0;
        break;
      
      }
}

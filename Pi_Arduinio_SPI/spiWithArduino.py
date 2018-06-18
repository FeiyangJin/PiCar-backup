#!/usr/bin/env python

import time,pigpio,struct


#open spi
pi = pigpio.pi()

if not pi.connected:
   exit(0)

h = pi.spi_open(0, 40000)


#tell arduino we are going to read a float
def getReadyForReadFloat():
   pi.spi_write(h,b'\x02')


#function that reads the float
def readFloat():
   
   print("we are ready for reading a float")
   
   (count1,byte1) = pi.spi_read(h,1)

   (count2,byte2) = pi.spi_read(h,1)

   (count3,byte3) = pi.spi_read(h,1)

   (count4,byte4) = pi.spi_read(h,1)

   result = struct.unpack('f', bytes([byte4[0],byte3[0],byte2[0],byte1[0]]))
   print("The float is",result[0])


#function for communicating with arduino
def communicate():
   while True:
      #first send byts to arduino
      #pi.spi_write(h,b'\x03\x05')
      time.sleep(1)
      
      getReadyForReadFloat()
      
      (count,data) = pi.spi_read(h,1)
      if data[0] == 35:
         readFloat()
      elif data[0] != 35:
         print("Fail to read the float")



if __name__ == '__main__':
   try:
      communicate()
   except:
      pi.spi_close(h)
      pi.stop()

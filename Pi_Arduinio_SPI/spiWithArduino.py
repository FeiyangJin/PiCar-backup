#!/usr/bin/env python

import time,pigpio


#open spi 
pi = pigpio.pi()

if not pi.connected:
   exit(0)

h = pi.spi_open(0, 40000)


#function for communicating with arduino
def communicate():
   while True:
      #first send byts to arduino
      pi.spi_write(h,b'\x03\x04')

      #sleep 1 second and read 1 byte
      time.sleep(1)
      #pi shoudl receive 0x08, which is sent from arduino
      #spi_read returns a tuple, first is the number of bytes read,
      #second is the byte array contains the bytes
      (count,data) = pi.spi_read(h,1)
      print("we get %s" % data)


if __name__ == '__main__':
   try:
      communicate()
   except:
      pi.spi_close(h)
      pi.stop()
      


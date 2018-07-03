#!/usr/bin/env python

import time,pigpio,struct

#open spi
pi = pigpio.pi()

if not pi.connected:
   exit(0)

spiSpeed = 1000000
h = pi.spi_open(0, spiSpeed)


byteNumber = 1000
loopNumber = 10
byteCount = 0
readCount = 0

def readManyBytes():
   global byteCount
   for i in range(0,byteNumber):
      (count,byte) = pi.spi_xfer(h,[1])
      byteCount = byteCount + 1


#function for communicating with arduino
def communicate():
   global readCount
   global byteCount
   startTime = time.time()
   while readCount < loopNumber:
      readManyBytes()
      readCount = readCount + 1
   endTime = time.time()
   print("we read %i bytes in %f seconds" % (byteCount,(endTime - startTime)))
   print("Each loop we try to read %i bytes, we execute %i loop" % (byteNumber,loopNumber))
   print("SPI speed we set is:",spiSpeed)


if __name__ == '__main__':
   try:
      #communicate()
      start = time.time()
      for i in range(0,10000):
         (count,byte) = pi.spi_xfer(h,[1,2,3,4])
      end = time.time()
      print(end - start)
   except Exception as e:
      print("Exception message:" + str(e))
      pi.spi_close(h)
      pi.stop()

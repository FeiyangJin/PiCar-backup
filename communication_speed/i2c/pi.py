import smbus
import time
import struct

byteNumber = 1000
loopNumber = 10
bus = smbus.SMBus(1)
byteCount = 0
readCount = 0
# This is the address we setup in the Arduino Program
address = 0x04


def readManyBytes():
   global byteCount
   for i in range(0,byteNumber):
      byte = bus.read_byte(address)
      byteCount = byteCount +1
      
   #print("we read %i bytes" % byteCount)
   #byteCount = 0


def communicate():
   global readCount
   global byteCount
   startTime = time.time()
   while readCount < loopNumber:
     # sleep one second
     # time.sleep(1)
     readManyBytes()
     readCount = readCount + 1
   endTime = time.time()
   print("we read %i bytes in %f seconds" % (byteCount,(endTime - startTime)))
   print("Each loop we read %i bytes, we execute %i loop" % (byteNumber,loopNumber))


if __name__ == '__main__':
   try:
      communicate()
   except Exception as e:
      print("error message: " + str(e))
      print("end")

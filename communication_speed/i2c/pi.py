import smbus
import time
import struct

bus = smbus.SMBus(1)
 
# This is the address we setup in the Arduino Program
address = 0x04


def read100Bytes():
   for i in range(0,100):
      byte = bus.read_byte(address)
      print(byte)


def communicate():
   while True:
     # sleep one second
     time.sleep(1)
      
     read100Bytes()



if __name__ == '__main__':
   try:
      communicate()
   except Exception as e:
      print("error message: " + str(e))
      print("end")

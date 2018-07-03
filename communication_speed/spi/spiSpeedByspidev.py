import spidev
import time
import pigpio

byteNumber = 10000
speed = 500000

inputData = []
def communicate():
   global speed,inputData
   while True:
      speed = int(input("Give the speed of spi "))
      if not speed:
         continue
      
      spi = spidev.SpiDev()
      spi.open(0,0)

      spi.max_speed_hz = speed
      to_send = [0x02]
      start = time.time()
      for i in range(0,byteNumber):
         spi.xfer(to_send)
         # inputData.append(spi.xfer(to_send)[0])

      end = time.time()
      print("Time used: %f for %i bytes under speed %i" % ((end - start),byteNumber,speed))
      spi.close()
      #for element in inputData:
      #   print(element)
      #print(len(inputData))
      #inputData = []


if __name__ == '__main__':
   try:
      communicate()
   except Exception as e:
      spi.close()
      print("Exception message:" + str(e))

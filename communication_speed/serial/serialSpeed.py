## Author: Feiyang jin
## Email: feiyang.jin@wustl.edu
## Organization: Washington University in St. Louis
## Date: July 2018
import serial
import time

#arduino port on raspberry pi, typically ttyACM0 or ttyACM1
ser = serial.Serial('/dev/ttyACM0')
ser.baudrate = 3000000
byteNumber = 1000000
loopNumber = int(byteNumber / 5)


def sayHello():
    for i in range(0,loopNumber):
        ser.write(b'hello')


def communicate():
    while True:
        var = int(input("please enter a int to trigger "))
        start = time.time()
        sayHello()
        end = time.time()
        print("To send %i bytes, we use %f seconds" % (byteNumber,(end - start)))


if __name__ == '__main__':
   try:
      communicate()
   except Exception as e:
      print("Exception message:" + str(e))
      ser.close()

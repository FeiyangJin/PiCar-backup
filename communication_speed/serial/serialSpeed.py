import serial
import time

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

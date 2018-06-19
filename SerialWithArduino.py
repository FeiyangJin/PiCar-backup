import serial
import pigpio
import time
import struct

##ser = serial.Serial('/dev/ttyACM0', 9600)
##
##
##def communicate():
##    while True:
##        line = ser.readline()
##        print(line)

pi = pigpio.pi()
arduino = pi.serial_open("/dev/ttyACM0",9600)


def readFloat():
    if pi.serial_data_available(arduino) > 3:
        (count,data) = pi.serial_read(arduino,4)
        result = struct.unpack('f', bytes([data[3],data[2],data[1],data[0]]))
        print("we received a float",result[0])


def communicate():
    while True:
        if pi.serial_data_available(arduino) > 0:
            inputByte = pi.serial_read_byte(arduino)
            if inputByte == 35:
                readFloat()
        time.sleep(1)


if __name__ == '__main__':
   try:
      communicate()
   except Exception as e:
      print("Exception message:" + str(e))
      pi.serial_close(arduino)
      pi.stop()
      

# -*- coding: utf-8 -*
import serial
import time
import datetime
import sys
import csv
sys.version[0] == '3' #declare for python 3

ser = serial.Serial("/dev/ttyS0", 115200) #serial port for Lidar
filename = 'LidarData.csv'

def getTFminiData():
    while True:
        time.sleep(1)
        count = ser.in_waiting
        #print("hello")
        #print(count)
        if count > 8:
            recv = ser.read(9)   
            ser.reset_input_buffer() 
            # type(recv), 'str' in python2(recv[0] = 'Y'), 'bytes' in python3(recv[0] = 89)
            # type(recv[0]), 'str' in python2, 'int' in python3 
            
            if recv[0] == 0x59 and recv[1] == 0x59:     #python3
                distance = recv[2] + recv[3] * 256
                #strength = recv[4] + recv[5] * 256
                #print('(', distance, ',', strength, ')')
                ser.reset_input_buffer()
                #open csv file and write, tip: newline = '' is necessary
                with open(filename,"a",newline = '') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                    currentTime = str(datetime.datetime.now()); #timestamp data
                    row = [currentTime,distance] #the row being written to csv file
                    spamwriter.writerow(row)
                    print(row)


if __name__ == '__main__':
    try:
        if ser.is_open == False:
            ser.open()
        getTFminiData()
    except KeyboardInterrupt:   # Ctrl+C
        if ser != None:
            ser.close()

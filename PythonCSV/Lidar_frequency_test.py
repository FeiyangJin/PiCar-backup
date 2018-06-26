#!/usr/bin/env python
# -*- coding: utf-8 -*

import serial
import time
import datetime
import sys
import csv
import threading
import sys
from IMU_SETUP import lib

sys.version[0] == '3' #declare for python 3

ser = serial.Serial("/dev/ttyS0", 115200) #serial port for Lidar

filename = 'Lidar_Frequency.csv'

timeDiffer = []

def getData():
    global lasttime
    currentTime = time.time()
    while currentTime - startTime < 10:
        currentTime = time.time()
        if ser.in_waiting > 8:
            #TFmini data
            recv = ser.read(9)
            ser.reset_input_buffer()

            if recv[0] == 0x59 and recv[1] == 0x59:
                distance = recv[2] + recv[3] * 256
                ser.reset_input_buffer()
                #print("Distance is:%i" % (distance))
                
                diff = time.time() - lasttime;
                timeDiffer.append(diff)
                #print(diff)
                lasttime = time.time()

    print("start writing")
    with open(filename,"a",newline = '') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(timeDiffer)):
            row = [timeDiffer[i]]
            spamwriter.writerow(row)
        

startTime = time.time()
lasttime = time.time()
if __name__ == '__main__':
    try:
        if ser.is_open == False:
            ser.open()
        getData()
    except KeyboardInterrupt:   # Ctrl+C
        if ser != None:
            ser.close()
        sys.exit()

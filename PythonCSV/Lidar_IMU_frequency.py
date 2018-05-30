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
filename = 'Lidar_IMU_New_Data.csv'

timeDiffer = []
rowList = []
def getData():
    global lasttime
    #connect with IMU
    imu = lib.lsm9ds1_create()
    lib.lsm9ds1_begin(imu)
    if lib.lsm9ds1_begin(imu) == 0:
        print("Failed to communicate with LSM9DS1.")
        quit()
    lib.lsm9ds1_calibrate(imu)

    current = time.time()
    while current - startTime < 10:
        
        current = time.time()
        if lib.lsm9ds1_accelAvailable(imu) > 0 and ser.in_waiting > 8:
            lib.lsm9ds1_readAccel(imu)
            ax = lib.lsm9ds1_getAccelX(imu)
            ay = lib.lsm9ds1_getAccelY(imu)
            az = lib.lsm9ds1_getAccelZ(imu)
            cax = lib.lsm9ds1_calcAccel(imu, ax)
            cay = lib.lsm9ds1_calcAccel(imu, ay)
            caz = lib.lsm9ds1_calcAccel(imu, az)
            gx = lib.lsm9ds1_getGyroX(imu)
            gy = lib.lsm9ds1_getGyroY(imu)
            gz = lib.lsm9ds1_getGyroZ(imu)
            cgx = lib.lsm9ds1_calcGyro(imu, gx)
            cgy = lib.lsm9ds1_calcGyro(imu, gy)
            cgz = lib.lsm9ds1_calcGyro(imu, gz)
            #TFmini data
            recv = ser.read(9)
            ser.reset_input_buffer()

            if recv[0] == 0x59 and recv[1] == 0x59:
                distance = recv[2] + recv[3] * 256
                ser.reset_input_buffer()
                currentTime = str(datetime.datetime.now()); #timestamp data
                row = [currentTime,distance,cax,cay,caz,cgx,cgy,cgz] #the row being written to csv file, just x and y accel
                rowList.append(row)
                #diff = time.time() - lasttime
                #timeDiffer.append(diff)
                #print(diff)
                #lasttime = time.time()
                #print(row)

    print("start writing")
    with open(filename,"a",newline = '') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(rowList)):
            row = [rowList[i]]
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

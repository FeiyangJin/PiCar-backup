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

filename = 'IMU_speed.csv'

timeDiffer = []

caxl = []
cayl = []
cazl = []
cgxl = []
cgyl = []
cgzl = []
def getData():
    global lasttime
    #connect with IMU
    imu = lib.lsm9ds1_create()
    lib.lsm9ds1_begin(imu)
    if lib.lsm9ds1_begin(imu) == 0:
        print("Failed to communicate with LSM9DS1.")
        quit()
    lib.lsm9ds1_calibrate(imu)

    while time.time() - startTime < 10:
        beforeIf = time.time()
        if lib.lsm9ds1_accelAvailable(imu) > 0:
            afterIf = time.time()
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

##            #add to list
##            caxl.append(cax)
##            cayl.append(cay)
##            cazl.append(caz)
##            cgxl.append(cgx)
##            cgyl.append(cgy)
##            cgzl.append(cgz)
            #print(cax,cay,caz,cgx,cgy,cgz)
            #diff = time.time() - lasttime
            timeDiffer.append(time.time() - lasttime - afterIf + beforeIf)
            #print(time.time() - lasttime)
            lasttime = time.time()

    print("start writing data")
    with open(filename,"a",newline = '') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(timeDiffer)):
            #row = [caxl[i],cayl[i],cazl[i],cgxl[i],cgyl[i],cgzl[i]]
            row = [timeDiffer[i]]
            spamwriter.writerow(row)

startTime = time.time()
lasttime = time.time()
if __name__ == '__main__':
    try:
        getData()
    except KeyboardInterrupt:   # Ctrl+C
        if ser != None:
            ser.close()
        sys.exit()

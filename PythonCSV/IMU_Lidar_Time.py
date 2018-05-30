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
filename = 'Lidar_IMU_Data.csv'

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec) 
        func()  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def sayHello():
    print('hello')
    print(datetime.datetime.now())
    
    
def getData():
    #connect with IMU
    imu = lib.lsm9ds1_create()
    lib.lsm9ds1_begin(imu)
    if lib.lsm9ds1_begin(imu) == 0:
        print("Failed to communicate with LSM9DS1.")
        quit()
    lib.lsm9ds1_calibrate(imu)
    while True:
        #get IMU accel data
        global lasttime
        
        #new structure testing
        if lib.lsm9ds1_accelAvailable(imu) > 0 and ser.in_waiting > 8:
            lib.lsm9ds1_readAccel(imu)
            ax = lib.lsm9ds1_getAccelX(imu)
            ay = lib.lsm9ds1_getAccelY(imu)
            cax = lib.lsm9ds1_calcAccel(imu, ax)
            cay = lib.lsm9ds1_calcAccel(imu, ay)
            #TFmini data
            recv = ser.read(9)
            ser.reset_input_buffer()

            if recv[0] == 0x59 and recv[1] == 0x59:
                distance = recv[2] + recv[3] * 256
                ser.reset_input_buffer()
                currentTime = str(datetime.datetime.now()); #timestamp data
                row = [currentTime,distance,cax,cay] #the row being written to csv file, just x and y accel
                diff = time.time() - lasttime;
                print(diff)
                lasttime = time.time()
                print(row)
                
            
        #old structure
##        while lib.lsm9ds1_accelAvailable(imu) == 0:
##            pass
##        lib.lsm9ds1_readAccel(imu)
##
##        ax = lib.lsm9ds1_getAccelX(imu)
##        ay = lib.lsm9ds1_getAccelY(imu)
##        #az = lib.lsm9ds1_getAccelZ(imu)
##
##        cax = lib.lsm9ds1_calcAccel(imu, ax)
##        cay = lib.lsm9ds1_calcAccel(imu, ay)
##        #caz = lib.lsm9ds1_calcAccel(imu, az)
##        #get TFmini data and write to file
##        count = ser.in_waiting
##        if count > 8:
##            recv = ser.read(9)   
##            ser.reset_input_buffer() 
##            
##            if recv[0] == 0x59 and recv[1] == 0x59:     #python3
##                distance = recv[2] + recv[3] * 256
##                ser.reset_input_buffer()
##                currentTime = str(datetime.datetime.now()); #timestamp data
##                row = [currentTime,distance,cax,cay] #the row being written to csv file, just x and y accel
##                print(row)
##                #print(datetime.datetime.now())
##                #open csv file and write, tip: newline = '' is necessary
####                with open(filename,"a",newline = '') as csvfile:
####                    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
####                    currentTime = str(datetime.datetime.now()); #timestamp data
####                    row = [currentTime,distance,cax,cay] #the row being written to csv file, just x and y accel
####                    #spamwriter.writerow(row)
####                    print(row)
                    

lasttime = time.time()
if __name__ == '__main__':
    try:
        if ser.is_open == False:
            ser.open()
        #set_interval(getData,0.02)
        #set_interval(sayHello,0.02)
        
        getData()
    except KeyboardInterrupt:   # Ctrl+C
        if ser != None:
            ser.close()
        sys.exit()

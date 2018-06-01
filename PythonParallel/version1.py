#!/usr/bin/env python
# -*- coding: utf-8 -*
from multiprocessing import Pool
import time
import picamera
import datetime
import serial
import sys
import csv
import threading
from IMU_SETUP import lib

frames = 20
sys.version[0] == '3'
ser = serial.Serial("/dev/ttyS0", 115200)
filename = 'Sensors_read_time.csv'
datafile = 'Sensors_data.csv'
timeDiffer = []
rowList = []


def getIMU():
    global imu
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
    return (cax,cay,caz,cgx,cgy,cgz)


def getLidar():
    #TFmini data
    recv = ser.read(9)
    ser.reset_input_buffer()

    if recv[0] == 0x59 and recv[1] == 0x59:
        distance = recv[2] + recv[3] * 256
        ser.reset_input_buffer()
        return distance

def getData():
    global start
    global imu
    global lasttime
    while time.time() - start < 10:
        if lib.lsm9ds1_accelAvailable(imu) > 0 and ser.in_waiting > 8:
            IMUdata = getIMU()
            Lidardata = getLidar()
            currentTime = str(datetime.datetime.now());
            row = [currentTime,Lidardata,IMUdata[0],IMUdata[1],IMUdata[2],IMUdata[3],IMUdata[4],IMUdata[5]]
            rowList.append(row)
            diff = time.time() - lasttime
            timeDiffer.append(diff)
            lasttime = time.time()

    print("start writing sensors data")
    with open(datafile,"a",newline = '') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(rowList)):
            row = [rowList[i]]
            spamwriter.writerow(row)

    print("start writing sensors reading frequency")
    with open(filename,"a",newline = '') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(timeDiffer)):
            row = [timeDiffer[i]]
            spamwriter.writerow(row)
            
    return 1

            
def f(x):
    global start
    while time.time() - start < 5:
        y = x*x
    print("for f function, total time elasped is:%f" % (time.time() - start))
    return x*x


def filenames():
    frame = 0
    while frame < frames:
        name = datetime.datetime.now()
        yield '%s.jpg' % name
        frame = frame + 1


def capture():
    startC = time.time()
    while time.time() - startC < 10:
        with picamera.PiCamera(resolution=(480,480), framerate=40) as camera:
            camera.start_preview()
            # Give the camera some warm-up time
            time.sleep(3)
            camera.capture_sequence(filenames(), use_video_port=True)
    return 1



imu = lib.lsm9ds1_create()
lib.lsm9ds1_begin(imu)
if __name__ == '__main__':
    if lib.lsm9ds1_begin(imu) == 0:
        print("Failed to communicate with LSM9DS1.")
        quit()
    lib.lsm9ds1_calibrate(imu)
    if ser.is_open == False:
        ser.open()
    
    start = time.time()
    lasttime = time.time()
    pool = Pool()
    sensors = pool.apply_async(getData)
    camera = pool.apply_async(capture)
    #result1 = pool.apply_async(f,[4])
    #result3 = pool.apply_async(capture)
    #answer1 = result1.get()
    #answer2 = result3.get()
    #sensorAnswer = sensors.get()
    cameraAnswer = camera.get()
    end = time.time()
    print("total time is %f" % (end - start))

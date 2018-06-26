from PIL import Image
import os
import csv

dataIndex = 0
filePath = "/home/pi/ok/camera/"


def display():
    global dataIndex
    time = dataList[dataIndex][0]
    IMU = dataList[dataIndex][2]
    imageName = filePath + dataList[dataIndex][8]
    image = Image.open(imageName)
    print("Time:%s IMU:%s" %(time,IMU))
    image.show()
    image.close()


def communicate():
    global dataIndex
    time = dataList[dataIndex][0]
    IMU = dataList[dataIndex][2]
    imageName = filePath + dataList[dataIndex][8]
    image = Image.open(imageName)
    print("Time:%s IMU:%s" %(time,IMU))
    image.show()
    image.close()
    while True:
        value = (int)(input("enter 1 for next moment, 0 for prev moment "))
        if value == 1:
            dataIndex = dataIndex + 1
            if dataIndex < len(dataList):
                display()
            elif dataIndex >= len(dataList):
                print("no next moment")
        elif value == 0:
            dataIndex = dataIndex - 1
            if dataIndex >= 0:
                display()
            elif dataIndex < 0:
                print("no previous moment")


if __name__ == '__main__':
    dataTimes = []
    dataList = []
    with open('/home/pi/Desktop/sync_data.csv',newline = '') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            dataTimes.append(row[0])
            dataList.append(row)
    try:
        communicate()
    except Exception as e:   # Ctrl+C
        print(str(e))

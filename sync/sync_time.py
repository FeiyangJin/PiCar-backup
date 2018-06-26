import os
import re
import csv

#match a photo to a set of data based on best-fit on time
def findBestFit(imageTime,dataList,startIndex):
    difference = abs(imageTime - (float)(dataList[startIndex][0]))
    currentIndex = startIndex
    #print(startIndex)
    #go through datalist, extract time, and compare the difference
    #we want to find the closest one for this imageTime
    for index in range(startIndex,len(dataList)):
        dataTime = (float)(dataList[index][0])
        newDiffer = abs(imageTime - dataTime)
        if newDiffer < difference:
            difference = newDiffer
            currentIndex = index

    #print("for this image, we match it to ",currentIndex)
    #print("The time difference is:",difference)

    #push file name to dataList
    imageName = str(imageTime) + ".jpg"
    if len(dataList[currentIndex]) == 8:
        dataList[currentIndex].append(imageName)


#if a photo is not matched, we try to find the previous matched one
def findPrevImage(dataList,index):
    aIndex = index
    FindImage = 1
    while len(dataList[index]) != 9:
        index = index - 1
        if index < 0:
            FindImage = 0
            break;

    if FindImage:
        ImageName = dataList[index][8]
        #add it to orignial element
        dataList[aIndex].append(ImageName)
        return 1
    elif not FindImage:
        return 0


#we try to find the next matched photo
def findNextImage(dataList,index):
    aIndex = index
    FindImage = 1
    while len(dataList[index]) != 9:
        index = index + 1
        if index > len(dataList) - 1:
            FindImage = 0
            break;

    if FindImage:
        ImageName = dataList[index][8]
        #add it to orignial element
        dataList[aIndex].append(ImageName)
        return 1
    elif not FindImage:
        return 0


fileNames = os.listdir("/home/pi/ok/camera")

#imageTime = re.compile(r"^[^.j]*")
imageTime = re.compile(r"^.*(?=(\.jpg))")

fileTimes = []
#extract photo time from its name,
#which is in the format: time.jpg
#and save it as a float for future comparison
for file in fileNames:
    theTime = imageTime.match(file)
    fileTimes.append((float)(theTime.group(0)))

fileTimes = sorted(fileTimes)


dataTimes = []
dataList = []
#read all data, which in the format [time,lidar,imu]
with open('/home/pi/ok/Lidar_IMU_Data.csv',newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        dataTimes.append(row[0])
        dataList.append(row)
        #print('data time:',row[0])


#sychrnoize image and data based on time
for index in range(len(fileTimes)):
    findBestFit(fileTimes[index],dataList,index)


#now give un-matched data a time
for index in range(len(dataList)):
    if len(dataList[index]) == 8:
        result = findPrevImage(dataList,index)
        if result == 0:
            findNextImage(dataList,index)


#write new data into a new csv file 
print("start writing csv file")
with open('sync_data.csv',"a",newline = '') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for data in dataList:
        spamwriter.writerow(data)

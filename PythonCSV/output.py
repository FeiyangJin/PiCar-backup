#!/usr/bin/python3
import csv
import datetime
print("Hello world")

# a is different from w, w will overwrite if the file already exits
# a will add content to the end of file

#file = open("outputFile.txt","w")

#file.write(str(datetime.datetime.now())) #how to convert datetime to string

#file.close()


#csv file output practice
csvName = 'csvSample.csv'
csvTitle = ['Time','Name','Birth']
name = ['josh','tom','lexie','david']
birth = ['11/21/1997','2/6/1960','5/29/1998','7/10/2004']
# for i in range(len(name)):
#     print(name[i])

with open(csvName,"w",newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(csvTitle)
    
    for i in range(len(name)):
        currentTime = str(datetime.datetime.now());
        row = [currentTime,name[i],birth[i]]
        spamwriter.writerow(row)

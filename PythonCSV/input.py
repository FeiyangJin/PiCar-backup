#!/usr/bin/python3
import csv

# str = input("Please enter input：\n")
# print("Input:", str)

filename = "sample.txt"


# with open(filename) as f:
#     for line in f:
#         line_contents = line.strip()
#         print(line_contents)


file = open(filename,"r")
line = file.readline()
i = 1
while line:
    print("The line %d is: %s" % (i,line))
    line = file.readline()
    i = i + 1

file.close()


#csv file input
csvName = "csvSample.csv"
with open(csvName, "r",newline='') as csvfile:
    spamreader = csv.reader(csvfile,delimiter = ",")
    for row in spamreader:
        print('  '.join(row))

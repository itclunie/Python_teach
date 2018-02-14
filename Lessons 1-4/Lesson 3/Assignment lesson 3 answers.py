import csv, os, sys


csvPath = os.path.abspath('csvLesson3.csv')


with open(csvPath, 'r') as inputt:                     # r instead of w
    reader = csv.reader(inputt, lineterminator = '\n') # we're using the csv.reader method
    for row in reader:
        csvList = list(reader)                             # use python's list method to dump all of reader's rows into a new list
##
##        csvList = []                                       # you can use also use the below method to get rows into a list
##        for row in reader:
##            csvList.append(row)
    
for row in csvList:
    print row

f = open('csv2text.txt','w')    #make your new txt file
for row in csvList:             #iteratre through your list
    for item in row:
        f.write(str(item) + ' ')    #have to convert the row list to string, \n means 'newline'
    f.write('\n')
f.close()

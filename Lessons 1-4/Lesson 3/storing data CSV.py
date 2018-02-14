import csv, os, sys

##csvPath = r'J:\Shared\J6\Constellation\CIIC\Geospatial\Workspace\Clunie\PythonPerl\Lessons\Lesson 3\csvLesson3.csv'
csvPath = os.path.abspath('csvLesson3.csv')

headers = ['header1','header2','header3']
csvlist1 = ['row two','row three', 'row four']
csvlist2 = ['row two','row three', 'row four']
csvlist3 = ['row two','row three', 'row four']
toplist = [headers,csvlist1,csvlist2,csvlist3]




#creates the CSV, will overwrite it each time the script is run. 'r' in place of 'w' will read, 'a' will append
##with open(csvPath, 'w') as output:
##    writer = csv.writer(output,lineterminator = '\n')
##    writer.writerow(['Header'])
##    
##    for item in csvlist1:
##        writer.writerow([item])


# comment out the csv creator code above and uncomment all the code below. Run it and see the changes.
        
with open(csvPath, 'w') as output:
    writer = csv.writer(output,lineterminator = '\n')
    
    for item in toplist:
        writer.writerow(item)

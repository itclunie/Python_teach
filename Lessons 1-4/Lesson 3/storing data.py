##"r"   Open a file for read only 
##"w"   Open a file for writing. If file already exists its data will be cleared before opening. Otherwise new file will be created 
##"a"   Opens a file in append mode i.e to write a data to the end of the file 
##"wb"   Open a file to write in binary mode 
##"rb"   Open a file to read in binary mode 
import os, sys

#here we're using a random variable
f = open('testinput.txt','w')
f.write('wrote new line1 \n')
f.write('wrote new line2 \n')
f.write('wrote new line3 \n')
f.close()



f = open('testinput.txt','r')
print f.read()
f.close()



f = open('testinput.txt','a')
f.write('appended line1 \n')
f.write('appended line2 \n')
f.close()  


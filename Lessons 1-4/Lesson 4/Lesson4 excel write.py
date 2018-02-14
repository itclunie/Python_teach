import xlwt, os, sys
from readXL_methods import readXL_method1
from readXL_methods import readXL_method2
from writeXL_method import writeXL_method

help(xlwt)


file_location = os.path.abspath('InputWorkbook.xls')


dataout = readXL_method1(file_location,'Sheet1') #same as xlrd lesson

for item in enumerate(dataout): #python enumerate function just counts your list elements
    print item


#**************we'll now use the xlwt (write) method to fill a new excel doc*************************

writeXL_method(dataout,'OutputSheet','OutputWorkbook') #supply our custom-made function its arguments (ie inputs)

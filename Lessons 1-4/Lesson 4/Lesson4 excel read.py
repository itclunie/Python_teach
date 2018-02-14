import xlrd
from readXL_methods import readXL_method1
from readXL_methods import readXL_method2

help(xlrd)

file_location = r"\\nnee05s1\cluniei\config\user\cluniei_NGOS.pds\Desktop\Lesson 4\InputWorkbook.xls"
workbook = xlrd.open_workbook(file_location)

sheet1 = workbook.sheet_by_name('Sheet1')
##sheet1 = workbook.sheet_by_index(0)       #other way to get a sheet

print sheet1.cell_value(0,0)    #how to get individual cell value
print sheet1.ncols              #get total num of columns/rows as an integer
print sheet1.nrows
print range(sheet1.nrows)       #the range() python method goes over ever number in a larger number. eg range(4) 1,2,3,4


for header in range(sheet1.ncols):      #iterate over each cell in a row
    print sheet1.cell_value(0,header)


for row in range(sheet1.nrows):         #iterate over each cell in a column 
    print sheet1.cell_value(row,0)


print sheet1.row_values(0) #get the same as above but returns these values packaged into a list
print sheet1.col_values(0)


total_cells = sheet1.ncols * sheet1.nrows #get total number of cells in your range, eg excel range A1:B4 has 8 cells
print total_cells



dataout = readXL_method2(file_location,'Sheet1') #supply our custom-made function its arguments (ie inputs)


for item in dataout:
    print item

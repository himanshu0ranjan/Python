'''
Created on Jul 26, 2017

@author: Himanshu Ranjan
'''
import openpyxl

wb = openpyxl.load_workbook('C:\\PythonExFiles\\example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
tuple(sheet['A1':'C3'])
#print(tuple(sheet['A1':'C3']))

for rowOfCellObj in sheet['A1':'C3']:
    for cellObj in rowOfCellObj:
        print(cellObj.coordinate(), cellObj.value)
    print('-----END OF ROW-----')
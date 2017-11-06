'''
Created on Jul 25, 2017

@author: Himanshu Ranjan
'''
import openpyxl

wb = openpyxl.load_workbook('C:\\PythonExFiles\\example.xlsx')
print(type(wb))

sheetNames = wb.get_sheet_names()
print(sheetNames)

sheet = wb.get_sheet_by_name('Sheet1')
print(sheet)
print(type(sheet))
print(wb.get_active_sheet())
print(sheet['A1'])
print(sheet['A1'].value)
c = sheet['B1']
print(c.value)
print('Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value)


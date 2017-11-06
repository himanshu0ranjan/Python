'''
Created on Jul 25, 2017

@author: Himanshu Ranjan
'''

import os
print(os.getcwd())

# opening the file
helloFile = open('C:\PythonExFiles\hello.txt','r')
# reading the file
helloContent = helloFile.read()
print(helloContent)
someFile = open('C:\PythonExFiles\hello1.txt','r') 
someContent = someFile.readlines()
print(someContent)

appendFile = open('C:\PythonExFiles\hello1.txt','a')
appendFile.write('\nThis is the new line appended in this file.')
appendFile.close()

newFile = open('C:\PythonExFiles\hello1.txt','r')
print(newFile.read())

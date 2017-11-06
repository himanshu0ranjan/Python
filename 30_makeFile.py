'''
Created on Jul 25, 2017

@author: Himanshu Ranjan
'''
import os

currentDir = os.getcwd()
print(currentDir)
os.chdir(os.path.join(currentDir,'Example Files'))
exampleDir = os.getcwd()
print(exampleDir)
os.makedirs(os.path.join(exampleDir, 'file1.txt'))
print(os.listdir(exampleDir))
print(os.getcwd())
'''
Created on Jul 25, 2017

@author: Himanshu Ranjan
'''
import os

currentDir = os.getcwd()
print(currentDir)
os.makedirs(os.path.join(currentDir, 'Example Files'))
madeDir = os.path.basename(currentDir)
print(madeDir)

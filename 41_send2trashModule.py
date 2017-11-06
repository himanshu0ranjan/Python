'''
Created on Jul 25, 2017

@author: Himanshu Ranjan
'''
import send2trash

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable')

baconFile.close()
send2trash.send2trash('bacon.txt')
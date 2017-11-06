'''
Created on Jul 25, 2017

@author: Himanshu Ranjan
'''

import time, subprocess

timeLeft = 10
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1
    
subprocess.Popen(['start', 'F:\\Backups\\Lenovo A6000 Plus - SD card\\VidMate\\download\\Badtameez_Dil.mp3'], shell=True)

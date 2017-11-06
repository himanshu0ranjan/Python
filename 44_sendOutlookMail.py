'''
Created on Sep 13, 2017

@author: Himanshu Ranjan
'''
import psutil
import os
import subprocess
import win32com.client as win32

def send_notification():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'youremail@example.com'
    mail.Subject = 'Message subject'
    mail.Body = 'Message body'
    mail.HTMLBody = '<h2>HTML Message body</h2>' # this field is optional
    mail.send

#In case you want to attach a file to the email
#attachment  = "Path to the attachment"
#mail.Attachments.Add(attachment)

#mail.Send()

# Open Outlook.exe. Path may vary according to system config
# Please check the path to .exe file and update below
     
def open_outlook():
    try:
        subprocess.call(['C:\Program Files (x86)\Microsoft Office\root\Office16\OUTLOOK.EXE'])
        os.system("C:\Program Files (x86)\Microsoft Office\root\Office16\OUTLOOK.EXE");
    except:
        print("Outlook didn't open successfully")
 
# Checking if outlook is already opened. If not, open Outlook.exe and send email
for item in psutil.pids():
    p = psutil.Process(item)
    if p.name() == "OUTLOOK.EXE":
        flag = 1
        break
    else:
        flag = 0
 
if (flag == 1):
    send_notification()
else:
    open_outlook()
    send_notification()

print('Mail Sent')
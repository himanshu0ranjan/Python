'''
Created on Jul 26, 2017

@author: Himanshu Ranjan
'''
import smtplib

# Connecting to an SMTP server
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
print(type(smtpObj))
# saying "Hello" to SMTP
smtpObj.ehlo()
# start encryption by calling starttls
smtpObj.starttls()
# Logging in to the SMTP server
mailPass = input('Enter the password to login in to the mail')
smtpObj.login('youremail@gmail.com', mailPass)
smtpObj.sendmail('youremail@gmail.com', 'ccemail@gmail.com', 'Subject: Hello Email \nHello Himanshu, Good evening!')
smtpObj.quit()


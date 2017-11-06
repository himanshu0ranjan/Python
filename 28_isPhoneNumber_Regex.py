'''
Created on Jul 25, 2017

@author: Himanshu Ranjan
'''
import re 
name = input("Enter your name :")
phoneNumber = input("Enter your phone number for example in +91 845-082-0742 format:")
str1 = 'your name is '+name+' and phone number is '+phoneNumber
isPhoneNumber = re.compile(r'\+\d\d \d\d\d-\d\d\d\-\d\d\d\d')
mo = isPhoneNumber.search(str1)
print("Your phone number is: "+mo.group())

'''
Created on Jul 27, 2017

@author: Himanshu Ranjan
'''

# textMyself.py - Defines the textmyself() function that texts a message passed to it as a string

from twilio.rest import Client

# Preset values
accountSID = 'your__twillo_account_SID'
authToken = 'your__twillo_account_auth_token'
myTwilioNumber = '+91XXXXXXXXXX'
myCellPhone = '+91XXXXXXXXXX'

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=myTwilioNumber, to=myCellPhone)
    
    
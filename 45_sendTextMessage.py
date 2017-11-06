'''
Created on Jul 27, 2017

@author: Himanshu Ranjan
'''

from twilio.rest import Client

accountSID = 'your_generated_account_SID'
authToken = 'your_generated_auth_token'

twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+91XXXXXXXXXX'
myCellPhone = '91XXXXXXXXXX'
message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you here.', from_=myTwilioNumber, to=myCellPhone)



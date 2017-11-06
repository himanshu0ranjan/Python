'''
Created on Jul 26, 2017

@author: Himanshu Ranjan
'''
import imapclient, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True, ssl_context=context)
mailPass = input('Please enter the mail password: ')
imapObj.login('automatepgm@gmail.com', mailPass)
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(u'SUBJECT "Hello"')
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
import pprint
pprint.pprint(rawMessages)
import pyzmail 
message = pyzmail.PyzMessage.factory(rawMessages[2][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('cc'))
print(message.get_addresses('bcc'))

if message.text_part !=None:
    print(message.text_part.get_payload().decode(message.text_part.charset))
elif message.html_part != None:
    print(message.html_part.get_paload().decode(message.html_part.charset))
else:
    print('Message body is not in either text or html format. Please check the mail')

# code to delete the message
imapObj.select_folder('INBOX', readonly=False)
UIDs = imapObj.search(u'SUBJECT "Google Account"')
imapObj.delete_messages(UIDs)
print(imapObj.expunge())

#disconnecting from the IMAP server

imapObj.logout()
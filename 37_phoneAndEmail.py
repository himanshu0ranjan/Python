'''
Created on Jul 25, 2017

@author: Himanshu Ranjan
'''
# This program finds the phone numbers and email address on the clipboard.
# would be useful if you have the boring task of finding every mail and phone number on a web page

import re 
import pyperclip 


# Step 1: Create a Regex for Phone Numbers

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                    # area code
    (\s|-|\.)?                            # separator
    (\d{3})                               #first 3 digits
    (\s|-|\.)                             # separator
    (\d{4})                               # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?        # extension
#    )''')
#    )''', re.VERBOSE)

# Step 2: Create a Regex for Email addresses

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                # username
    @                                # @ symbol
    [a-zA-Z0-9.-]+                   # domain name
    (\.[a-zA-Z]{2,4})                # dot-something
    )''')                            
#    )''', re.VERBOSE)
    

# Step3 : Find all the matches in the clipboard text

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
    
# Step 4: Join the matches into a string for the clipboard


if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

                        

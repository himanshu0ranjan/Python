#! python3.6
# mapIt.py - launches a map in the browser using an address from the command line or clipboard
'''
Created on Jul 28, 2017

@author: Himanshu Ranjan
'''
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ''.join(sys.argv[1:])
else:
    #print(sys.argv)
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


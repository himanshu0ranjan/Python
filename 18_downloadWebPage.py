#
'''
Created on Jul 28, 2017

@author: Himanshu Ranjan
'''

import requests

res = requests.get('http://www.gutenberg.org/files/26268/26268-readme.txt')
#res = requests.get('https://www.brainyquote.com/quotes/topics/topic_work.html')
print(type(res))
#print(res.status_code== requests.codes) 
print(len(res.text))
print(res.text[:250])

playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)


try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
    
playFile.close()
#
'''
Created on Jul 28, 2017

@author: Himanshu Ranjan
'''
import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
elems = exampleSoup.select("#author")
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

spanElem = exampleSoup.select('span')[0]
print(str(spanElem))
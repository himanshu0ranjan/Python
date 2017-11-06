from urllib.parse import urljoin
'''
Created on Aug 11, 2017

@author: Himanshu Ranjan
'''

import requests, bs4, os, smtplib

# Start of the Weather Forecast Block
resW = requests.get('https://weather.com/en-IN/weather/today/l/INXX0300:1:IN')
resW.raise_for_status()

# Start html parser
weatherSoup = bs4.BeautifulSoup(resW.text, "html.parser")
# weatherElem = weatherSoup.select('.today_nowcard-temp span')
weatherText = weatherSoup.select('.today_nowcard-main')
if not weatherText:
    print('Could not find today\'s weather forecast...Sorry :(')
else:
    print('Today''s temperature:', weatherText[0].text)
    print('Weather String From HTML Parsing', weatherText[0])

#import libraries
import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re
import ssl

# ignore ssl certificate errors
certification = ssl.create_default_context()
certification.check_hostname = False
certification.verify_mode = ssl.CERT_OPTIONAL

# Enter url link
url = input('Enter URL Here: - ')
html = urllib.request.urlopen(url,context = certification).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrives the url data from the specified html span tags.
# Retrieve all of the span tags
tags = soup('span')
Sum = 0
Count = 0
for tag in tags:
   num = tag.contents[0]
   #print (num)
   Sum = Sum + int(num)
   Count = Count + 1
   
print('Count',Count )  
print('Sum',Sum)

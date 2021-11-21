#import libraries
import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re
import ssl

# ignore ssl certificate errors
certification = ssl.create_default_context()
certification.check_hostname = False
certification.verify_mode = ssl.CERT_NONE

# Enter url link
url = input('Enter URL Here: - ')
html = urllib.request.urlopen(url,context = certification).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrives the url data from the specified html anchor tags.
tags = soup('a')

count = input('Enter count number: ')
count = int(count)
pos = input('Enter position number: ')
pos = int(pos)

print('Retrieving:',url)
#lookup for each anchor tags  
for tag in tags:
        #check the index position
        if (tags.index(tag) <= pos):
                tag = tag.get('href',None)
                print('Retrieving:',tag)
                
                #print('Count:',count)
                count = count -1
                if count < 0:
                        print('Red flag:',count, 'count is finish!')
                        break
        else:
                continue
                
                
        
        

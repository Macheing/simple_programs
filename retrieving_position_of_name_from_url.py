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

# Retrives the url data from the specified html anchor tags.
tags = soup('a')

count_num = input('Enter count number: ')
count_num = int(count_num)
position = input('Enter position number: ')
position = int(position)
lst = list()

for tag in tags:
        tag.decode().strip()
        tag = str(tag).strip('<a">').replace('href="',' ').replace('">',' ').rstrip('</')
        tag = tag.split()
        href = tag[0].split()
        name = tag[1].split()
        #print(tag)
        lst.append(tag)
        
        
for i in range(len(lst[:position])):
        name = lst[i]
        names = str(name).strip("[']").replace("'",'')
        print('Retrived:',names)
        if i == position:
                #print(names)
                break

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
count_last_name = dict()

for tag in tags:
        tag.decode().strip()
	#print(tag)
        name = re.findall(('[A-Z].+'),str(tag))
        print(name)
        last_name = str(name).strip('[]').strip("'").strip('</a>').replace('">',' ').split()
        #print(last_name)
        clean_name = last_name.remove(last_name[0])
        #print(type(last_name))
        #last_name = str(last_name).strip('[]').strip("'")
        #last_name = last_name.split()
        #print(last_name)
        
        
        for name in last_name:
                count_last_name[name] = count_last_name.get(name,0)+1
        
print(max(count_last_name.items()))
print('Minimum Last Name Encountered:',min(count_last_name.items()))
print(count_last_name)
        
        

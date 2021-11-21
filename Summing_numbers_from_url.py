#import libraries for scraping purpose
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

#dealing with ssl certificates errors
certify = ssl.create_default_context()
certify.check_hostname = False
certify.verify_mode = ssl.CERT_NONE

#open URL 
url = input('Enter your URL here:- ')
html = urlopen(url,context=certify).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all digits from the html file
Sum = 0
count = 0
nums = soup('span')
#print(type(nums))
#print(nums)

for num in nums:
        num.decode().strip()
        data = re.findall('[0-9]+',str(num))
        #print(type(data))
        #print(data)
        string = str(data)
        string = string.strip('[]').replace("'","")
        Sum = Sum + int(string)
        count += 1
        print('Data:',data,'Digit:',string,'Sum',Sum)
print('Count:',count)
print('Sum:',Sum)


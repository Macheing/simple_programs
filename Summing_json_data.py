import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    Sum = 0
    count = 0
    url = input('Enter url here: - ')
    if len(url) < 1: break
    js = urllib.request.urlopen(url, context=ctx).read()
    #print(js)
    data = js.decode()
    #print(data)
    js_data = json.loads(data)

    items = js_data['comments'][0:50]
    for item in items:
        num = item['count']
        count += 1
        Sum += num
        #print(num)
    print('Sum:',Sum, 'Count:',count)
   
           

    

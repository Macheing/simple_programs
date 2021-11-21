name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    line.rstrip()
    if not line.startswith("From "):
		continue
	
    dic = line.split()
    #print(dic)
    words = dic[5]
    #print(words)
    times = words[:2]
    #print(times)
    hours = times.split(':')
    #print(hours)
    
    for time in hours:
	#accummodate words and their frequencies
        count[time] = count.get(time,0) + 1
          
#print(count)
    
data = None
for key,value in count.items():
	data = sorted(count.items())
	#print(data)
for k,v in data:    
		print(k,v)
#print(type(data))
        
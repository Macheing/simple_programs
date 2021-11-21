#import urllib.request
file_handler = open("mbox-short.txt")
#print(file_handler)
count = 0
for line in file_handler:
	count += 1
	linex = line.rstrip()
	print(linex)

print('Number of lines:', count)
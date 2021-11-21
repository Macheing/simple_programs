import re
handler = open("regex_sum_1212477.txt","r")
sum = 0
count = 0
# extracting digits within a content of a file
nums = re.findall('[0-9]+',handler.read())
#print(type(nums))
#print(nums)
#loop through extracted elements
for num in nums:
	#convert each data element from str to int
        data = int(num)
	#sum up the total number of digit found
        sum = sum + data
	#count the number of digits found in a file.
        count +=1
print('Sum:',sum,'Count:',count)
	
largest = None
smallest = None
print('Type "done" to end the program')
while True:
	nums = input("Enter a number: ")
	if nums == 'done':
		break
	try:
		num = int(nums)
		print(num)

		for num in nums:
			if num > largest:
				largest = num
			else:
			smallest = num
	except:
		print("Invalid input")
		continue
	
		
print("Maximum is", largest)
print("Minimum is", smallest)
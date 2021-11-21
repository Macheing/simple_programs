# this program asks users to enter numbers and counts number of entries.
# calculates sum and average of user's entries number.

count = 0 	#count
total = 0.0 	#sum
print('Enter "Done" to end program')

# as program run
while True:
	# ask user for a number
	val = input("Enter a number: ")
	# end program when user enter Done
	if val == "Done":
		print("User finish entering values")
		break
	#convert user's vlaue to float values
	try:
		vals = float(val)
		print(vals)
	#if converion fails, alert user and continue execution.
	except:
		print("Invalid: you enter non-numeric value!")
		continue

	#counts number of entries
	count += 1
	#add the total number of entry values
	total += float(val)
	#computes the average of entries
	average = total/count

print()
print("|Counts: ",count, " |","Sum: ",total, "  |", "Average: ",average, "  |")
#print("Counts:", count)
#print("totals:", total)
#print("Average:", average)
print("All done!")


	
#Ask usser for file name
name = input("Enter file:")
#check user's file length.
if len(name) < 1 :
    name = "mbox-short.txt"
#file handler
handle = open(name,'r')
#dictionary 
counts = dict()

#loops through the lines of user's file
for line in handle:
    #narrow search to sentences begin with 'From'
    #or otherwise skip that line to next line.
    if not line.startswith('From '):
        continue
    
    #removes newlines of each line.
    lines = line.rstrip()
    #print(lines)
    
    #split and convert strings into list
    linex = lines.split()
    #print(linex)
    
    #extracts senders from the original list into a new list
    words = linex[1:2]
    #words = str(word).strip("[']")
    #print(words)
    
    #convert list into dictionary and populate it with keys & values.
    for key in words:
		counts[key] = counts.get(key,0)+ 1

#check the content of dictionary
#count = counts.items()
#print(count)
		
freq_number = None	#highest encountered value
freq_word = None	#highest encountered word or key.

#finds most frequent key and value
for key,value in counts.items():
    #check if highest encoutered is none
    #or the current value is greater than encountered value.
    if freq_number is None or value > freq_number:
        freq_number = value		
        freq_word = key
        
#print out word with highest values
print(freq_word,freq_number)

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
average = 0.0
data = 0.0
for line in fh:
    line = line.strip()
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
 
    line = line.replace("X-DSPAM-Confidence:",'')
    count += 1
    data = float(line) + data
    average = float(data)/count
    
    #print(line)
    #print(data)
    #print(average)
    
# average spam detection
print("Average spam confidence:", average)

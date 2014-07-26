#Program for writing into file. Ex #16
print "Enter the filename:",
filename=raw_input()

print "Opening the file..."
print "text in the file:"
name=open(filename)
print name.read()
name.close()
print "Opening file in write mode..."
name=open(filename,'w')

print name.truncate()

print "Enter three lines of your choice:"
line1=raw_input("Line 1: ")
line2=raw_input("Line 2: ")
line3=raw_input("Line 3: ")
print "Writing these lines to the file..."
 
name.write(line1+"\n")
name.write(line2+"\n")
name.write(line3+"\n")
print "Closing the file..."
name.close()


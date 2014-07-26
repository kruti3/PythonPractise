#code for exercise 17: Copy content from one file to another

from os.path import exists 	#essential in order to use exists
f1=raw_input("Enter the source file name: ")
f2=raw_input("Enter the destination file name: ")

o1=open(f1)
print "Contents of source file:"
clip=o1.read()
print clip

print "Destination file exists: %r" % exists(f2)

o2=open(f2,'w')	#open destination file in write mode
o2.write(clip)

print "The contents have been copied from %s to %s successfully" %(f1,f2)

o2.close()
o1.close()
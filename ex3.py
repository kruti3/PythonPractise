print "Enter the filename: "
name=raw_input("> ")
txt=open(name)

print "The contents of the file are:"

print txt.read()

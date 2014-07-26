#command line arguments
from sys import argv

prompty= "> "
script, one, two, three=argv
print "The script is called ", script
print "Command line arguments are: %r %r %r" %(one, two, three)

print "Answer my question!"
ans=raw_input(prompty)


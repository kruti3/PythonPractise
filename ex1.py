#This is exercise 1 from learnpythonthehardway.org
#1.Printing a specific line
import random

f = open('ex1.py')
#Reading lines of the file into a list 
arr = f.readlines()
#Counting number of lines
k = len(arr)
#Generating a random number
x = random.randrange(0,k)
print arr[x]
f.close()

#1)
#a. We've covered how to do the "for" loop in lesson 1, now we'll look at another
# type of "for" loop and the "while" loop.

#Iterate through each value in a number
for PosNum in range(10):
    print PosNum

print '\n' 


#b. Iterate through a numeric range. We're going over each number between 1 & 10
for PosNum in range(3,10):
    print PosNum

print '\n' 


#2)
#a. The advantage of using the above "for loop" form with a python list
# is the ability to see it's position (ie index) in the list, for example
exampleList = ['a','b','c','d','e','f','g']

#remember this function: len(someList). We can use it with the above range() method
print len(exampleList)

print '\n'

#so here we're going over each element in a list by using it's index
for PosNum in range(len(exampleList)):
    print exampleList[PosNum]

print '\n'

#b. Just like in the above section 1)b. we can go through a set range, in this case index 
for PosNum in range(3, len(exampleList)):
    print exampleList[PosNum]


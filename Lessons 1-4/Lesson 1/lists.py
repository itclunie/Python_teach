##the python list. The feature I use most in pyton. Think of it as a CD rack, starting at position zero

##position  0   1   2  etc
sublist = ['q','r','x']
listExample = ['a', 'b', 'c', 'd', 12, sublist] #so 'a' is position 0, 'b' is 1, etc.

print len(listExample)
print listExample


#run through each item in a list, ie iteration
for item in listExample: 
    print item


##Accessing elements in list. Remember each element has a position?
print listExample[0] #Well you can tell Python to access that position
print listExample[1]
print listExample[5]


print 'a' in listExample #find stuff in your list

if 'a' in listExample: #or do it this way
    print 'True'
else:
    print 'False'
    

##access only parts of the list, ie slice
print listExample[2:]  #this starts at position 2 and goes until end
print listExample[1:3]  #this starts at pos 1 and goes until pos 3


#most used list methods (important)
print len('python')

listExample.append('q')
print listExample


#mush n lists together using + operator 
listExample2 = [13,14,15]
listExample3 = listExample + listExample2
print listExample3


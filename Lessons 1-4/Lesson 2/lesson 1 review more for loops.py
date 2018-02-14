#just to cement the for loop, here are some more examples:

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []

for thing in list1:
    if thing > 5:
        print thing

print '\n'


for thing in list1:
    if thing > 5 and thing < 9:
        print thing

print '\n'


for thing in list1:
    if thing != 5:
        list2.append(thing)

print list2

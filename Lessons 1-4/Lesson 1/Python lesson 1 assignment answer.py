

#1.

A = 50
B = 100
C = 51
##C = 29
    

#i) Write an if statement that says if A is less than B, print both A and B's values

#ii) Edit this statement to say if A is less than B but greater than C, print 'A < B, A > C'.
#   Google 'python elif' and incorporate it into this if statement, ie:
#       if A is less than B but greater than C, do action
#       else if A is less than B and A less than C, do action

if A < B:
    print A
    print B

if A < B and A > C:
    print 'A < B and A > C'
elif  A < B and A < C:
    print 'A < B and A < C'


#2.
#i) Create one empty list and one list filled with the following values:
#   Billy, Suzy, Bobby, Horracio, Annie

#ii) Write a loop that tests if each element equals Annie or Bobby.
#   If yes, print that element and add it to the empty list you made (hint append method)
list1=[]
list2=['Billy', 'Suzy', 'Bobby', 'Horracio', 'Annie']

for item in list2:
    if item == 'Annie' or item == 'Bobby':
        list1.append(item)

print list1

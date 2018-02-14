#the python numerical operators. they work just like youd think

##+ adition can add numbers but also concatenate strings. 
print 1 + 1
print 'string1' + 'string2'



##- and * and / work as expected. remaining operators require some explanation:

## Exponentiation Operator 
print 2 ** 3 # is same as 2 * 2 * 2


##% operator this returns remainder after division
## Can be useful for seeing if a number is even or odd
print 7 % 2


#Greater/less than are as expected (> and <). 
x = 40
n = 41
if n != x: #this is the DoesNotEqual operator
    print n

#or this way
if not n == x: #note the == is different from the =. = is for assigning variables, == is for interogating them
    print n
    

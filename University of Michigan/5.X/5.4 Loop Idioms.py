#Counting in a loop

zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15] : #thing is the iteration variable
    zork = zork + 1
    print(zork, thing)
print("After", zork)

#To count how many times we execute a loop, we introduce a counter variable that starts at 0 and we add one to it
#each time through the loop

#Summing in a Loop

zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print("After", zork)

#To add up a value we encounter in a loop, we introduce a sum variable that starts at 0 and we add the value to the
#sum each time through the loop. So that's how we compute totals.

#Finding the average in a Loop

count = 0
sum = 0
print("Before", count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count)

#An average just combines the counting and sum patterns and divides when the loop is done.

#Filtering in a Loop

print("Before")
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20:                      #filtering pattern
        print("Large number", value)
print("After")

#We use an if statement in the loop to cach / filter the values we are looking for.

#Search using a Boolean Variable
#You got integer variables, you got string variables, you got floating-point variables.
#Boolean variable is a kind of variable that either has the True or False

found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True        #found is a mnemonic variable
    print(found, value)
print("After", found)

#If we just want to search and know if a value was found, we use a variable that starts at False and is set to True
#as soon as we find what we are looking for.

# How to find the Smallest Value

smallest_so_far = 10000 #This is a flag value
print("Before", smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num < smallest_so_far :
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

print("After", smallest_so_far)

#I did it right but it's the wrong approach

#There is a variable called none type, None. And it only has one constant in it.
#Booleans have True or False, integers have a whole bunch, and the floats have a whole bunce. And non-types have one
#thing, none.

#Finding the smallest Value

smallest = None             #None is a flag Value
print("Before")
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value    #The first time, 9 is comming in here
    elif value < smallest :
        smallest = value
    print(smallest, value)

print("After", smallest)

#We still have a variable that is the smallest so far. The first time through the loop smallest is None, so we take
# the first value to be the smallest.

#This techniqe is a good way to do the largest and the smallest, to usse ths None, and then have a little bit of code
#that triggers the first time to the loop to get you sort of a loop carried variable setup.

#The "is" and "is not" Operators

smallest = None
print("Before")
for value in [3, 41, 12, 9, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)

print("After", smallest)

#Python has an "is operator that can be used in logical expressions
#Implies "is the same as"
#Similar to, but stronger than ==
#"is not" also is a logical operator



#The is operator is stronger than the equality operator (==) as it insists on matching the two values exactly
# including type. This simple example shows the difference: >>> 1.0 == 1 True >>> 1.0 is 1 False While 1.0 is the
# same value after the integer 1 is converted to floating point, the is operator does no conversion and so the two
# values do not match. The is operator is best used on small constant values like small integers, True, False, and None.
# The is operator should not be used with large numeric values or strings - these values should be compared with
# the == operator
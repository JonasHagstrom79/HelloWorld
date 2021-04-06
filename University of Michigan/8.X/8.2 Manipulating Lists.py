#8.2 Manipulating Lists

#Concatenating Lists Using +
#We can create a new list by adding two existing lists together

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)

#Lists Can Be Sliced Using :

t = [9, 41, 12, 3, 74, 15]
#    0   1   2  3   4   5
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
#Remember: Just like in strings, the second number is "up to but not including

#List Methods

x = list()
print(x)
print(dir(x))

#Building a List From Scratch

#We can create an empty list and then add elements using the "append" method
#The list stays in order and new elements are added at the end of the list

stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)
stuff.append("cookie")
print(stuff)

#Is Something in a List?

#Python provides two operators that let you check if an iten is in a list
#These are locical operators that return True or False
#They do not modify the list

some = [1, 9, 21, 10 ,16]
if 9 in some:
    print("True")
if 15 in some:
    print("False")
if 20 not in some:
    print("True")

#Lists are in Order

#A list can hold many items and keeps those items in the order until we do somethong to change the order
#A list can be sorted (i.e., change its order)
#The "sort" method (unlike in strings) means "sort yourself"

friends = [ "Joseph", "Glenn", "Sally"]
friends.sort()
print(friends)
print(friends[1])

#Built-in Functions and Lists

#There are number of functions built into Python that take lists as parameters
#Remember the loops we built? These are much simpler

nums = [3, 41, 12, 9, 74, 15]
nums.sort()
print(nums)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#Two ways to do the same

#1st(old) with loop, thisone just stores one number in the memory, better if you use over 100K numbers
total = 0
count = 0
while True :
    inp = input("Enter a number: ")
    if inp == "done" : break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count

print("Average:", average)

#2nd(new) with list(data structure), this one stores all the numbers in memory, doesnt matter if less than 100K numbers
#Also the best way if you already got the numbers in a list

numlist = list()
while True :
    inp = input("Enter a number: ")
    if inp == "done": break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print("Average:", average)









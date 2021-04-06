#8.1 Lists

#Programming
#Algorithms - A set of rules or steps used to solve a problem
#Data structures - A particular way of organizing data in a computer

#What is Not A "Collection"?
#Most of our variables have one value in them - when we put a new value in the variable, the old value is overwritten

# x = 2
# x = 4
# print(x)
# 4

#A List Is A Kinf Of Collection
#A collection allows us to put many values in a single "variable"
#A collection is nice because we can carry many values arround in one convenient package.

frineds = [ "Joseph", "Glenn", "Sally" ] #square brackets is list constant
carryon = [ "socks", "shirt", "perfume"] #this is now a list, not a string

#List Constants
#List constants are sorrunded by square brackets [] and the elements in the list are separated by commas ,
#A list element can be any Python object - even another list
#A list can be empty

print([1, 24, 76])
print(["red", "yellow", "blue"])
print(["red", 24, 98.6])
print([ 1, [5, 6], 7])
print([])

#We Already Use Lists!

for i in [5, 4, 3, 2, 1] :
    print(i)
print("Blastoff!")

#So lists and definite loops are best friends

friends = ["Joseph", "Glenn", "Sally"]
for friend in friends :
    print("Happy new year:", friend)
print("Done!")

z = ["Joseph", "Glenn", "Sally"]
for x in z:
    print("Happy New Year:", x)
print("Done!")
#The same code with different variable names above

#Looking Inside Lists
#Just like strings, we can get at any single element in a list using an index specified in square brackets[]

friends = [ "Joseph", "Glenn", "Sally"] #Joseph Glenn Sally
print(friends[1])                       #  0      1     2

#Lists Are Mutable(Changable)
#Strings are "immutable" - we cannot change the contents of a string - we must make a new string to make any change
#Lists are "mutable" - we can change an element of a list using the "index" operator

fruit = "Banana"
#fruit[0] = "b"

x = fruit.lower()
print(x)

lotto = [2, 14, 26 ,41, 63]
print(lotto)

lotto[2] = 28
print(lotto)

#How Long is a List?

#The "len()" function takes a list as a parameter and return the number of elements in the list
#Actually "len()" tells us the number of elements of any set or sequence (such as a string...)

greet = "Hello Bob"
print(len(greet))

x = [1, 2, "Joe", 99]
print(len(x))

#Using the Range Function
#The "range" function returns a list of numbers that range from zero to one less than a parameter
#We can construct an index loop using for and an intiger iterator

#print(range(4))

friends = ["Joseph", "Glenn", "Sally"]
print(len(friends))
print(range(len(friends)))

#A Tale of Two Loops...

friends = ["Joseph", "Glenn", "Sally"]
for friend in friends :
    print("Happy New Year;", friend)

for i in range(len(friends)) : #The range here is 0 1 2 and so the "i" is gonna go through 0 1 2
    friend = friends[i]
    print("Happy New Year;", friend) # A way to create a counted loop


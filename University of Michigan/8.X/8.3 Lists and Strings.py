#8.3 Lists and Strings

#Best Friends: Strings and Lists

abc = "With three words"
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
print(stuff)
for w in stuff : #w is an iteration variable and gonna loop throuh the string 3 times and print the words out each
    print(w)

#Split breaks a string into parts and produces a list of strings. We think of these as words. We can acess a particular
#word or loop through all the words

line = "A lot              of spaces"
etc = line.split()
print(etc)

line = "first;second;third"
thing = line.split()
print(thing)
print(len(thing))

thing = line.split(";") #Splits where the ";" is
print(thing)

print(len(thing))

#When you do not specify a delimeter, multiple spaces aer treated like one delimiter
#You can specify what delimiter charachter to use in the splitting

#Split to parse mail data

fhand = open("mbox-short.TXT")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From ") : continue #This is the skip-code
    words = line.split()
    print(words[2]) #Pulls out the second (3rd)
    
line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
words = line.split() #split() is based of the spaces
print(words)

#The Double Split Pattern

#Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again

line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
words = line.split()
email = words[1]
pieces = email.split("@") #Double split after the "@" (stephen.marquard@uct.ac.za)
print(pieces[1])                                     #           0          1

#List Summary
#Concept of a collection
#Lists and definite loops
#Indexing and lookup
#List mutability
#Functions: len, min, max, sum
#Slicing lists
#List methods: append, remove
#Sorting lists
#Splitting strings into lists of words
#Using split to parse strings

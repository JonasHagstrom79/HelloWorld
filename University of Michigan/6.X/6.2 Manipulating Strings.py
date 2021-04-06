#String Concatenation
#Whne the + operator is applied to strings, it means "concatenation"(hoplänka)

a = "Hello"
b = a + "There"
print(b)

c = a + " " + "There" # " " puts the space in
print(c)

#Using in as a Logical Operator
#The in keyword can also be used to check to see if one string is "in" another string
#The in expression is a logical expression that returns True or False and can be used in an if statement

fruit = "banana"
"n" in fruit    #True
"m" in fruit    #False
"nan" in fruit  #True
if "a" in fruit :
    print("Found it")

#String Comparison
word = "x"

if word == "banana" :
    print("All right, bananas.")

if word < "banana" :
    print("Your word, " + word + ", comes before banana.")
elif word > "banana" :
    print("Your word, " + word + ", comes after banana.")
else:
    print("All right, bananas.")

#Upper case letters sort befor lower case

#String Library
#Python has a number of string functions wich are in the string library
#These function are already built into every string - we invoke them by appending the function to the string variable
#These functions do not modify the original string, instead the return a new string that has been altered

greet = "Hello Bob"
zap = greet.lower() #make a copy of greet but all lower case and store that in zap, its not changing the original string
print(zap)
print(greet)
print("Hi there" .lower())

#Methods

stuff = "Hello world"
type(stuff)
dir(stuff) #https://docs.python.org/3/library/stdtypes.html#string-methods

#String library
#str.capitalize()
#str.center(width[, fillchar])
#str.endswith(suffix[, start[, end]])
#str.find(sub[, start[, end]])
#str.lstrip([chars])
#str.replace(old, new[, count])
#str.lower()
#str.rstrip([chars])
#str.strip([chars])
#str.upper()

#Searching a String
#We use the find() function to search for a substring within another string
#find() finds the first occurence of the substring
#If the substring is not found, find() returns -1
#Remember that string positions starts at zero

fruit = "banana"
pos = fruit.find("na")
print(pos)

aa = fruit.find("z")
print(aa)

#Making Everything UPPER CASE

#We can make a copy of a string in lower case or upper case
#Often whenwe are searching for string using find() we first convert the string to lower case so we can search a
#string regardless of case

greet = "Hello Bob"
nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www)

#Search And Replace
#The replace() function is like "search and repalce" operation in a word processor
#It replaces all occurrences of the search string with the replacement string

greet = "Hello Bob"
nstr = greet.replace("Bob", "Jane")
print(nstr)

nstr = greet.replace("o", "X")
print(nstr)

#Stripping Whitespace
#Sometimes we want to take a string and remove whitespace at the beginning and/or the end
#lstrip() and rstrip() remove whitespace at left and right
#strip() removes both beginning and ending whitespace

greet = "   Hello Bob   "
nstr = greet.lstrip()
print(nstr)
nstr = greet.rstrip()
print(nstr)
nstr = greet.strip()
print(nstr)

#Prefixes

line = "Please have a nice day"
line.startswith("Please")
#True
line.startswith("p")
#False

#Parsing and Extracting

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find("@")
print(atpos)
sppos = data.find(" ",atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

x = 'From marquard@uct.ac.za'
print(x[14:17])

#The iterator (loop) variable is the variable which stores a portion of the iterable when the for loop is being
# executed. Each time the loop iterates, the value of the iterator variable will change to a different portion
# of the iterable

print(len('banana')*7)
#String Data Type
#A string is a sequence of charachters
#A string literal uses quotes '' or ""
#For strings, + means "link"
#When a sring contains numbers, it is still a string
#We can convert numbers in a string into a number using int()

#Reading And Converting
#We prefer to read data in using strings and then parse and convert the data as we need
#This gives us more control over error situations and/or bad user input
#Input numbers must be converted from strings

#Looking Inside Strings
#We can get at any single charachter in a string using an index specificed in square brackets []
#The index value must be an integer and starts at zero
#The index value can be an expression that is computed

fruit = "banana"
letter = fruit[1] #We can actually pull each charachter out, we callt this the index operator[1] b a n a n a
print(letter)                                                                                 #  0 1 2 3 4 5

x = 3
w = fruit[x-1]
print(w)

#A Charachter Too Far
#You will get a python error if you attempt to index beyond the end of the string
#So be careful when constructing index values and slices

#Strings Have Lenght
#The built-in function len gives us the length of a string

fruit = "banana"
print(len(fruit))

#Len Function
#A function is some stored code that we use. A function takes some input and produces an output
#"banana"(a string) ---> len() (function) ---> 6 (a number)

#Looping Through Strings
#Using a while statement and an iteration variable, and the len function, we can construct a loop to look
#at each of the letters in a string individually

fruit = "banana"
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#Looping Through Strings
#A definite loop using a for statement is much more elegant
#The iteration variable is completely taken care of by the for loop

fruit = "banana"
for letter in fruit: #for = determined loop, and "is" is like member of for all the letter in the set fruit
    print(letter)

#They do the same(above, while and for), always go for the simplest(for) with least lines of code when possible

#Looping and Counting
#This is a simple loop that loops through each letter in a string and counts the number of times the loop encounters
#the "a" charachter

word = "banana"
count = 0
for letter in word :
    if letter == "a" :
        count = count + 1
print(count)

#Looking Deeper Into in
#The iteration variable "iterates" through the sequence (ordered set)
#The block (body) of code is executed once for each value in the sequence
#The iteration variable moves through all the values in the sequence

#for letter(iteration variable) in "banana"(six-charachter string)
#   print(letters)

#The iteration variable "iterates" through the string and the block(body) of code is executed once for each
#value in the sequence

#Slicing Strings
#We can also look at any continuous section of a string using a colon operator[]
#The second number is one beyond the end of the slice - "up to but not including"
#If the second number is beyond the end of the string, it stops at the end

#   Monty Pyth o  n
#   0123456789 11 12
s = "Monty Python"
print(s[0:4]) #up to but not including
print(s[6:7])
print(s[6:20]) #its ok to refer beyond the end of the string without getting an error

#If we leave off the first number or the last number of the slice, it is assumed to be the beginning or end
#of the string respectively

s = "Monty Python"
print(s[:2])
print(s[8:])
print(s[:])

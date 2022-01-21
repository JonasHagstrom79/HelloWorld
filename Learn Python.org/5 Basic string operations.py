#Basic string operations

string = "Hello world!"
print(string)
print(len(string)) #the length of string
print(string.index("o")) #the index of char o
print(string.count("l")) #counts the numbers char l
print(string[3:7]) #prints a slice, starting at index 3 and ending att index 6

print(string[3:7:2]) #This prints the characters of string from 3 to 7 skipping one character. This is extended
                    # slice syntax. The general form is [start:stop:step].

print(string[::-1]) #Reverses a string
print(string.upper()) #All chars to upper
print(string.lower()) #All chars to lower

print(string.startswith("Hello")) #If true then Python prints true
print(string.endswith("asdaaf")) #If false then Python prints false

afterwords = string.split(" ") #Splits the string and buch it into a list
print(afterwords)

#Excersise

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

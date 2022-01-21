#String formatting

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

#This prints out "Name" and "Age"

name = "John"
age = 23
print("%s is %d years old" % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

#EXERCISE

data = ("John", "Doe", 53.44)
format_string = "Hello"

print((format_string), "%s %s. Your current balance is $ %s." % data)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $ %s."

print(format_string % data)
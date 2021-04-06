print("Hello World")

#Lektion 2.2

#We can instruct Python to pause and read data from the user using the input() function
#The input() function returns a string

nam = input("Who are you?")
print("Welcome",  nam)

#string conversions
#You can also use int() and float() to convert between strings and integers

sval = "123"
type(sval)

ival = int(sval)
type(ival)
print(ival + 1)

#Convert elevator floors
inp = input("Europe floor?")
usf = int(inp) + 1
print("US floor" , usf)

#Question 8
x = 1 + 2 * 3 - 8 / 4
print(x)

#2.3 Write a program to prompt the user for hours and rate per hour using
# input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to
# test the program (the pay should be 96.25). You should use input to read
# a string and float() to convert the string to a number. Do not worry about
# error checking or bad user data.

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))
float(hrs)
float(rate)
pay = float(hrs * rate)
#pay = int(hrs) * 2.75
#rate = 2.75
#float(hrs * rate)
#print("Pay:"hrs * rate)
print("Pay:" , pay)

#You should use the built-in float() function to convert from a string to a float
#You should not include the input data in your source code. You must read the values for the rate and pay using input()
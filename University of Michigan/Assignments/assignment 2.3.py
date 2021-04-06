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

#Lärarens lösning nedan, input görs om till tal med float
xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
xp = float(xh) * float(xr)
print("Pay",xp)
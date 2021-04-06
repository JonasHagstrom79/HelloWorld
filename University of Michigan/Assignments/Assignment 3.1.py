#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly
# rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a
# rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and
# float() to convert the string to a number. Do not worry about error checking the user input - assume the user types
# numbers properly.

hrs = input("Enter Hours:")
rate = input("Rate:")
h = float(hrs)
r = float(rate)
pay = r * h
ot = r * 1.5

if h <= 40 : #här är jag fast, timmarna(h) istället för rate(r ska vara pay)
    pay = r * h
    print(pay)

if h > 40 :
    pay = r * 40
    overtime = ot * (h -40)
    print(pay + overtime)
#if h <= 40 :
#    r2 = r - 40
#    r2 = r2 * 1.5
#On the right track, need to add r and r2 to h separatly and then sum it up
#range
#pay1 = float(h) * float(r)
#pay2 = float(h - 40) * float(r2)

#print("Pay:", pay1 + pay2)

#for i in range(5) :
#    print (i)
#    if i > 2 :
#        print("Bigger than 2")
#    print("Done witn i", i)
#print("All done")

#Teachers solution
sh = input("Enter hours: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)
#print(fh, fr)
if fh > 40 :
    #print("Overtime")
    reg = fr * fh
    otp = (fh -40.0) * (fr * 0.5)
    #print(reg, opt)
    xp = reg + otp
else:
    # print("Regular")
    xp = fh * fr
print("Pay:", xp)
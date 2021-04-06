#Think about the blocks, one entrence and one exit
#Elif = Else If


#It´s gonna do the questions in order, cheking one at a time. The rule is, one of the three will run and the other two will not, it only triggers once
#
#x = float(input("Select a number of X"))
x = 0
if x < 2 :
    print("Small")
elif x < 10 :
    print("Medium")
else :
    print("Large")
print("All done")

#Remember it checks the elif´s in order
x = 15
if x < 2 :
    print("Small")
elif x < 10 :
    print("Medium")
elif x < 20 :
    print("Big")
elif x < 40 :
    print("Large")
elif x < 100 :
    print("Huge")
else :
    print("Ginormous")

#try-except is the code that Python will execute if something goes wrong, it checks the try in order and never goes back
#Minimize the lines in a try-except block
astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1

    print("First", istr)

astr = "123"
try:
    istr = int(astr)
except:
    istr = -1

print("Second", istr)

#Sample try / except

rawstr = input("Enter a number:")
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0 :
    print("Nice work")
else:
    print("Not a number")

#astr = 'Hello Bob'
#istr = int(astr)
#print('First', istr)
#astr = '123'
#istr = int(astr)
#print('Second', istr)
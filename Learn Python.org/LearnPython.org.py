#print("bla bla bla")

#x = 1
#if x ==1:
#    print("x is 1.")

#Variables and types


#myint = 12342345325325435
#print(myint)

myfloat = 7.0
print(myfloat)

#Simple operators can be executed on numbers and strings

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " +world
print(helloworld)

#Assignments can be done on more than one variable "simultaneously" on the same line like this

a, b = 3,4
print(a,b)

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)


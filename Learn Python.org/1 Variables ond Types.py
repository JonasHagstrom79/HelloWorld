#Numbers

#To define an integer, use the following syntax:

myint = 7
print(myint)

#To define a floating point number, you may use one of the following notations:

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

#Strings

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)


one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a,b)

#Exercise

# change this code
mystring = None
myfloat = None
myint = None

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
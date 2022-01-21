#Conditions

#Python uses boolean logic to evaluate conditions. The boolean values
# #True and False are returned when an expression is compared or evaluated.
# For example:

x = 3
print(x == 3)
print(x == 4) # == equals boolean, != not equal
print(x < 4)

#Boolean operators
#The "and" and "or" boolean operators allow building complex boolean expresions, for example:

name = "Jonas"
age = 42
if name == "Jonas" and age == 42:
    print("Your name is %s and you are also %d years old" %(name, age))

if name == "Jonas" or name == "Sven":
    print("Your name is either %s or Sven" %name)

#The "in" operator
#The in operator could be used to check if a specified object exists within an
#iterable object container, such as a list:

if name in ["Jonas", "Sven"]:
    print("Your name is either %s or Sven" %name)

#Python uses indentation to define code blocks, instead of brackets.
# The standard Python indentation is 4 spaces, although tabs and any other
# space size will work, as long as it is consistent. Notice that code blocks
# do not need any termination.

x = input("Input value of x: ")
if x == "2":
    print("x equals %s" %x)
else:
    print("x does not equal to %s" %x)

#The "is" operator
#Unlike the double equals operator "==", the "is" operator does not match the
# values of the variables, but the instances themselves. For example:

x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)

#The "not" operator
#Using "not" before a boolean expression inverts it:
print(not False)
print((not False) == (False))

#Exercise

number = 16
second_number = 10
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
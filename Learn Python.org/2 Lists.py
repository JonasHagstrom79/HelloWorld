# Lists

mylist = []
mylist.append("asafafasf")
mylist.append(2)
mylist.append(3)
print(mylist[0])  # prints 1
print(mylist[1])  # prints2
print(mylist[2])  # prints3

# prints out 1,2,3

for x in mylist:
    print(x)

# Exercise

numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings = []
strings.append("hello")
strings.append("world")
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1] #["Achmed", "Attatyrk", "Mahmoud"]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
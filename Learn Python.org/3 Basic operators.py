#Arithmetic Operators

number = 1 + 2 * 3 / 4.0
print(number)

#Modulo %, dividend % divisor = reminder

remainder = 11 % 3
print(remainder)

#using two multiplication symbols makes a power relationship

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

#Operators with strings

lotsofhellos = "hello" * 10
print(lotsofhellos)

#Operators with lists

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3]*3)

#Exercise

x = object()
y = object()

# TODO: change this code
x_list = [x,x,x,x,x,x,x,x,x,x] # [x] * 10
y_list = [y,y,y,y,y,y,y,y,y,y]
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
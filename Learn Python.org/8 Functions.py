#What are Functions?

#Functions are a convenient way to divide your code into useful blocks,
# allowing us to order our code, make it more readable, reuse it and save
# some time. Also functions are a key way to define interfaces so programmers
# can share their code.
import math


def my_function():
    print("Hello From My Function!")
username = "Bert"
greetings = "Hej"

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s" %(username, greeting))

def sum_two_numbers(a,b):
    return a + b

my_function()

#How do you call functions in Python?
#Simply write the function's name followed by (), placing any required arguments
# within the brackets.



def list_benefits():
      thislist = ["More organized code", "More readable code", "Easier code reuse",
    "Allowing programmers to share and connect code together"]
list_benefits()

import math

opti = 10e-5
count = 0

while count < 50:
    print(opti)
    opti += opti*math.log(10e6)/61
    count +=1


money = 100000
count = 0

while count <10:
    print("År %d: %d kronor" % (count ,money))
    money += money*1.08
    count +=1

#Building our own function
#We create a new function using the def keyword followed by optional paramenters in parentheses
#We indent the body of the function
#This defines the functionbut does not execute the body of the function

x = 5
print("Hello")

def print_lyrics() :
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day")
#You must invoke the function to print the def statement
print_lyrics()

x = x + 2
print(x)

#Arguments
#An argument is a value we pass into the function as its input when we call the function
#We use arguments so we can direct the function to do different kinds of work when we call it at different times
#We put the arguments in parentheses after the name of the function

# big = max("Hello world")

#Parameters
#A parameter is a variable wich we use in the function definition. It´s a "handle" that allows the code in the
#function to access the arguments for a particular function invocation


def greet(lang) :
    if lang == "es":
       return "Hola"
    elif lang == "fr":
       return "Bonjour"
    else:
        return "Hello"
print(greet("fr"), "Michael")
#Return Values
#Often a function will take its arguments, do some computation, and return a value tobe used as the value of the
# function call in the calling expression. The (return) keyword is used for this

def greet() :
    return "Hello"

print(greet(), "Glenn")
print(greet(), "Sally")

#Arguments, Parameters, and Results

#big = max("Hello world")
#print(big)

#def max(inp) :
#   blah
#   blah
#   for x in inp:
#       blah
#       blah
#   return "w" return is the execution statement in the paremer and send the value out

#Multiple Parameters / Arguments
#We can define more than one parameter in the function definition
#We simply add more arguments when we call the function
#We match the number and order of arguments and parameters

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)


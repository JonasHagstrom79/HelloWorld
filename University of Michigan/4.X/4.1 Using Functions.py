#store and reuse, D-R-Y dont repeat yourself. def is the new function
def thing() :
    print("Hello")
    print("Fun")

thing()
print("Zip")
thing()

#max function
big = max("Hello world")
print(big)
tiny = min("Hello world")
print(tiny)

#type conversions

print(float(99) / 100)

i = 42
type(i)

f = float(i)
print(f)

type(f)

print(1 + 2 * float(3) / 4 - 5)

#String Conversions, you can also use int() and flaot() to convert between strings and integers
#You will get an error if the string does not contain numeric characters

sval = 123
type(sval)
#class "str"
print(sval + 1)

ival = int(sval)
type(ival)
#class int
print(ival + 1)

#nsv = "hello bob"
#niv = int(nsv)
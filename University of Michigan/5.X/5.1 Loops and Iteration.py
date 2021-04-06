#repeated steps

n = 5
while n > 0 :
    print(n)
    n = n - 1
print("Blastoff!")
print(n)
#while is indefinite loops
#Loops(repeated steps) have iteration variables(to controll the loop) that change each time through the loop.
# Oftenthese iteration variables go through a sequence of numbers.

#infinite loop

#n = 5
#while n > 0 :
#    print("Lather")
#    print("Rinse")
#print("Dry off")

#Breaking out of a loop
#The break statement ends the current loop and jumps to the statement immediatley following the loop
#It is like a loop test that can happen anywhere in the body of the loop

while True:
    line = input("> ")
    if line == "done" :
        break
    print(line)
print("Done!")

#Finishing an Iteration with continue
#The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration

while True:
    line = input(">")
    if line[0] == "#" : #If the first charachter is # then continue the loop
        continue #abandons the current iteration and goes to the next iteration
    if line == "done" :
        break
    print(line)
print("Done!")


#Lecture 3

x = 5
if x < 10:
    print("Smaller")
#if statements always end with a colon
if x > 20:
    print("Bigger")

print("Finis")

#Boolean expressions ask a question and produce a Yes or No result wich we use to control program flow
#Boolean expressions using comparison operators evaluate to True / False or Yes / No
#Comparison operators look at variables but do not change the variables

# < Less than
# <= Less than or Equal to
# == Equal to
# > Greater than
# >= Greater than or Equal to
# != Not equal
# Remeber "=" is used for assignment

x = 5
if x == 5:
    print("Equals 5")
if x > 4 :
    print("Greater than 4")
if x >= 5 :
    print("Greater than or Equals 5")
if x < 6 : print("Less than 6")
if x <= 5 :
    print("Less than or Equals 5")
if x != 6 :
    print("Not equal to 6")

#One-Way Decisions

x = 5
print("Before 5")
if x == 5 :
    print("Is 5")
    print("Is still 5")
    print("Third 5")
#Indenting runs all blocks down, to continue with the code tab back with backspace
print("Afterwards 5")
print("Before 6")
if x == 6 :
    print("Is 6")
    print("Is Still 6")
    print("Third 6")
print("Afterwards 6")

#increase/maintain after if or for decrease to indicate end of block

X = 5
if x > 2 :
    print("Bigger than 2")
    print("Still bigger")
print("Done with 2")

for i in range(5) :
    print (i)
    if i > 2 :
        print("Bigger than 2")
    print("Done witn i", i)
print("All done")

#Nested Decisions
x = 42
if x > 1 :
    print("More than one")
    if x < 100 :
        print("Less than 100")
print("All done")

#Two-way Decisions with else, it´s just gonna run one. And by doing so it´s not gonna run the other one
x = 4
if x > 2 :
    print("Bigger")
else :
    print("Smaller")
print("All done")

#Loops
#For and while loops in Python

#The "for" loop

primes = [2, 3, 5,7 ]
for prime in primes:
    print(prime)

#For loops can iterate over a sequence of numbers using the "range" and "xrange"
# functions. The difference between range and xrange is that the range function
# returns a new list with numbers of that specified range, whereas xrange returns
# an iterator, which is more efficient. (Python 3 uses the range function, which
# acts like xrange). Note that the range function is zero based.

for x in range(5):
    print(x)

for x in range(3,6):
    print(x)

for x in range(3, 8, 2):
    print(x)

#While loops
#While loops repeat as long as a certain boolean condition is met. For example:

count = 0
while count < 5:
    print(count)
    count += 1 #the same as count = count +1

#"break" and "continue" statements break is used to exit a for loop or a while loop,
# whereas continue is used to skip the current block, and return to the "for"
# or "while" statement. A few examples:

count = 0
while True:
    print(count)
    count +=1
    if count >= 11:
        break

#Prints out only odd numbers
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

#Can we use "else" clause for loops? Unlike languages like C,CPP.. we can use
# else for loops. When the loop condition of "for" or "while" statement fails
# then code part in "else" is executed. If a break statement is executed inside
# the for loop then the "else" part is skipped. Note that the "else" part is
# executed even if there is a continue statement.

count = 0
while(count<5):
    print(count)
    count+=1
else:
    print("Count value reached %d" %(count))

for i in range (1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("This is not printed because for loop is terminated because of break but not due to fail of condition")

#Exercise

#Loop through and print out all even numbers from the numbers list in the same
# order they are received. Don't print any numbers that come after 237 in the sequence.

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for i in numbers:
    if i % 2 == 0: #är jämt

        print(i)
    elif i == 237:
        break

   # if(i == 237)
   #     break:

print("Blubbor")
#Solution
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)
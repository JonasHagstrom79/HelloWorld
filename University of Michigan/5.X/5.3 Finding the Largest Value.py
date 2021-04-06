#Finding the largest value
print("Before")
for thing in [9, 41, 12, 3 ,74, 15] :
    print(thing)
print("After")

#What is the largest number?
#Findign the larges value
largest_so_far = -1 #before the loop
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] : #During the loop, (iteration variable)
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print("After", largest_so_far) #Payoff is after the loop

#We make a variable that contains the largest value we had seen so far. If the current number we looking are looking at
#is larger, it´s the new largest value we have seen so far.


#tot = 0
#for i in [5, 4, 3, 2, 1] :
#    tot = tot + 1
#print(tot)

#n = 0
#while n > 0 :
#    print('Lather')
#    print('Rinse')
#print('Dry off!')

#lst = []
#num = int(input('How many numbers: '))
#for n in range(num):
#    numbers = int(input('Enter number '))
#lst.append(numbers)
#print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))

largest  = None
smallest = None

while True:
    num = input("Enter a number:")
    if num == "finish" : break
    try:
        fnum = float(num)  #Convert input to float

        #Get largest value
        if largest is None:
            largest = fnum
        elif fnum > largest:
            largest = fnum

        #Get smallest value
        if smallest is None:
            smallest = fnum
        elif fnum < smallest:
            smallest = fnum

    except:
        #If the user input is not 'finish' or a number
        print("Invalid input")
        continue


print("Largest value is",largest)
print("Smallest value is",smallest)
#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for
# lines of the form: X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those
#values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
summa = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print(line)
    pos = line.find(":")
    number = line[pos+2:]
    value = float(number)
#Här är numret sparat, måste få det att addera nästa and so on      <<<<----------------HÄR


    summa = value + summa
#    value = value #+ total
    count = count + 1    #Det jag ska dela med(antal rader) som är 27
    #times = float(count)
    total = summa / float(count)


#    total = value

#total = times + number

    #print(value)


print("Average spam confidence:", total)
#print(count)
#print("Done")


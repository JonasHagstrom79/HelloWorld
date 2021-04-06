#Program calculates your age

birth_year = input("Birth year: ")

age = 2020 - int(birth_year)
print(age)

#Asks a user their weight (in pounds), convert it to kilograms and print on the terminal

weight_pounds = input("Your weight in pounds? ")
weight_kilograms = int(weight_pounds) * 0.45359237
print(weight_kilograms)

#Print Pi´s first five decimals

First_number = 7 * 7 * 7 * 7 * 7 * 7 * 7
Second_number = 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4 * 4
Pi = int(First_number) / int(Second_number)
print(Pi)

#4*(1 - (1/3) + (1/5) - (1/7)...) ~ Pi
iterationer = int(input("Hur många iterationer?"))
pi = 0
n = 1
t = 1
for i in range(iterationer):
	pi += (1/n)*t
	n += 2
	t = t*(-1)
	print(i+1, pi*4)

#Course = Python for beginners
course = "Python´s for beginners"
#         0123456
print(course[1])
#inom [] så visas det man säger med siffrorna endast -1 blir sista bokstaven i meningen
# exemplet [0:3] ger alla bokstäver 0 1 2, ej sista(3)
# another = course[:] kopierar hela strängen

name = 'Jonas'
print(name[1:-1])

#Formatted strings, example 1
first = 'Jonas'
last = 'Hagström'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)

#Räknar med len hur många bokstäver i en sträng
course = 'Python for Beginners'
print(len(course))
#course. funktinonen kan göra stora bokstäver för hela strängen
print(course.upper())
print(course.lower())
print(course)
#print(course.find('o')) räknar antal tecken
print(course.find('o'))
#print(course.replace('Beginners', 'noobs^^') byter ut orden/bokstäver i strängen
print(course.replace('Beginners', 'noobs'))
#print('Phyton' in course) för att få True eller False, man kan kontrollera om ordet finns
print('Python' in course)
#int är heltal float är decimaltal
print(10 - 3)
print(10 + 3)
print(10 / 3)
print(10 // 3)
#dubbel // blir int(heltal)
print(10 % 3)
print(10 ** 3)
# ** är samma som ^X
x = 10
x = x + 3
print(x)
#man kan även skriva samma som ovan på ett smidigare sätt
x = 10
x += 3
print(x)
#samt använda - * eller / istället om man vill
#operator president är ordningen man använder +-*/ i ekvationer
# parenteser
# exponenter
# multiplikation eller division
# addition eller subtraktion
x = 10 + 3 * 2 ** 2
print(x)

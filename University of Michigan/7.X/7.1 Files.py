#7.1 Files
#Opening a File

#Before we can read the content of a file, we want to tell Python wich file we are going to work with and what we
#will be doing with the file
#This is done with the open() function
#open() returns a "file handle" - a variable used to perform operations on the file
#Similar to "File -> Open" in a Word Processor

#Using open()

#handle = open(filename, mode)
#returns a handle use to manipulate the file
#filename is a string
#mode is optional and should ber "r" if we are planning to read the file and "w" if we are going to write to the file

#The newline Character

#We use a special character called the "newline" to indicate when a line ends
#We represent it as \n in strings
#Newline is still one character - not two

stuff = "Hello\nWorld"
print(stuff)

stuff = "X\nY"
print(stuff)


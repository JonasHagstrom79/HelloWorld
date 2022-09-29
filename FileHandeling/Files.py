# File Object

# Not recomended
# Default is open for reading "r", there is also write="w", appending="a", read&write="r+"
f = open("test.txt", "r")

print(f.name)
print(f.mode)

#close the file
f.close()

## Open a file using a context manager
with open("test.txt", "r") as f:
    #f_contents = f.read()
    #print(f_contents)
    #f_contents = f.readlines()
    #print(f_contents)

    # Line by line
    #f_contents = f.readline() # Grabs the first line of the file
    #print(f_contents, end="") # end to remove newline between the lines
    #f_contents = f.readline()  # Repeats and get the second line of the file this time
    #print(f_contents, end="")

    ## Iterate over the lines in the file (for extremly large files/memory problems)
    #for line in f:
    #    print(line, end="")

    # More controll to the reader
    #f_contents = f.read(100) # First 100 chars of the file
    #print(f_contents, end="")
    # Next 100 chars
    #f_contents = f.read(100)  # First 100 chars of the file
    #print(f_contents, end="")

    # Loop through large files
    size_to_read = 10
    f_contents = f.read(size_to_read)

    print(f.tell()) # Tells on wich char we are in the document

    while len(f_contents) > 0:
        print(f_contents, end="*") # * to visualize the data
        f_contents = f.read(size_to_read)


    ## Manipulating the position to read from
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end="")

    f.seek(0) # Starts all over from index 0

    f_contents = f.read(size_to_read)
    print(f_contents)

## Write to file
with open("test2.txt", "w") as f:
    f.write("Test") #Will create the file if its not created, WILL OVERWRITE EXISTING FILE IF ALREADY EXISTING
    #pass # = dont do anything
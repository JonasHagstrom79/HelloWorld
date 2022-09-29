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
    f.seek(0) # Overwrites the first Test with the 2nd. Doesnt delete the whole content
    f.write("Test")

## Make a copy of a file
with open("test.txt", "r") as rf: # rf = readfile
    # Create a copy
    with open("test_copy.txt", "w") as wf:  # wf = writefile
        for line in rf:
            wf.write(line)

## Make a copy of a picture
with open("cat-cupid-love-icon.png", "rb") as rf: # rf = readfile, rb = readBINARY, neede for picture
    # Create a copy
    with open("cat-cupid-love-icon_copy.png", "wb") as wf:  # wf = writefile, wf = writeBINARY
        for line in rf:
            wf.write(line)

## Make a copy of a picture chunk by chunk for more control
with open("cat-cupid-love-icon.png", "rb") as rf: # rf = readfile, rb = readBINARY, neede for picture
    # Create a copy
    with open("cat-cupid-love-icon_copy.png", "wb") as wf:  # wf = writefile, wf = writeBINARY
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            # Read in next chunc_size for not getting an infinite loop
            rf_chunk = rf.read(chunk_size)


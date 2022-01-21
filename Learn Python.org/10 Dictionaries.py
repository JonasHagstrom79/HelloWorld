#A dictionary is a data type similar to arrays, but works with keys and
# values instead of indexes. Each value stored in a dictionary can be
# accessed using a key, which is any type of object (a string, a number,
# a list, etc.) instead of using its index to address it.

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781#,
 #   "Jake": 938273443
}
# your code goes here
phonebook["Jake"] = 938273443
phonebook.pop("Jill")
print(phonebook)
# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
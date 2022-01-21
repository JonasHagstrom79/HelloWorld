from cryptography.fernet import Fernet

key = Fernet.generate_key()             #This generates a key, u have to use the same key to encrypt/decrypt something


inp = input("> ")
text = bytes(inp, "utf-8")

crypter = Fernet(key)
pw = crypter.encrypt(text) #(b"Mypassword")             #The "b" makes the string in bytes
decryptString = crypter.decrypt(pw)             #This decrypts the string



#print(pw)
#print(key)
print(str(pw, "utf-8"))                         #Removes the b' .... ' from the lines
print(str(decryptString, "utf-8"))

#testing
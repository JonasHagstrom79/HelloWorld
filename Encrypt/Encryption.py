#import
#data = input("> ")

#data = "Min fina gullesötis, puss puss puss"
#code = "abcdefghijklmnopqrstuvwxyzåäö"          #data.encode(encoding="UTF-32", errors="strict")
#decode = code.decode(decoding="UTF-32", errors="strict")
#crypt = data[0:-1] + code[+3]
#for code in [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, å, ä, ö ] :
#    data + code

#print(code)
#print(data)
#print(crypt)
#print(decode)

#----------------------------------------------------------------------------------------
#import base64

#data = input("> ")#"abc123!?$*&()'-=@~"

# Standard Base64 Encoding
#encodedBytes = base64.b64encode(data.encode("utf-8"))
#encodedStr = str(encodedBytes, "utf-8")

#print(encodedStr)

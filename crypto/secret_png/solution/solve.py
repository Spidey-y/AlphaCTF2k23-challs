from pwn import *
import string 


# 1st step : xoring bytes with printible chars to find key 

header =b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52"

charset= string.printable
key=""

with open("flag.png.xor","rb") as infile :
    file = infile.read()
    for i in range(len(header)):
        for c in charset:
            if header[i]== ord(xor(c.encode(),file[i])) :
                key+= c 
                print(key)
                break
    
    
# 2nd step : xoring the file with the found key
    key = "7h15_1s_my_k3y"

    with open("flag.png","wb") as outfile :
        outfile.write(xor(key,file))
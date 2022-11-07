import random

plaintext = input("enter a text")
x= plaintext
alphabet = 'abcdefghijklmnpoqrstuvwsyz1234567890'
key = ''.join((random.choice(alphabet)for x in range(250)))
print("This is the random key",key)

def encryption(string, key): 
  encrypt_text = ''
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])-32) %95 + 32 
    encrypt_text += chr(x) 
  return("" . join(encrypt_text))
print(encryption(x,key))
y = encryption(x,key)
file1 = open("cipher","w")
file1.write(y)
file3 =open("key","w")
file3.write(key)
def decryption(encrypt_text, key): 
  orig_text = ''
  for i in range(len(y)): 
    x = (ord(encrypt_text[i]) -ord(key[i]) -32) %95 +32 
    orig_text += chr(x)
  return("" . join(orig_text))
z = decryption(y,key) 
print(decryption(y,key))
file2 = open("decrypt","w")
file2.write(z)


file1.close()
file2.close()
file3.close()

print("This is the random key",key)
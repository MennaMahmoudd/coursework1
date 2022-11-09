# using import random to produce random values mainly in the key
import random
# let the user enter a text 
plaintext = input("enter a text")
# put the text that the user entered in a variable called x
x= plaintext
# From these letters and numbers the key is formed
alphandnum = 'abcdefghijklmnpoqrstuvwsyz1234567890'
# using random.choice to returns randomly letters and numbers for the key
# using for to repeat selecting letters and numbers for the key for specific number
key = ''.join((random.choice(alphandnum)for x in range(50)))
# printing output the random key
print("This is the random key",key)

# defining a function encryption and naming two arguments 
def encryption(string, key): 
  encrypt_text = ''
# using for loop in the range of the length in string
  for i in range(len(string)): 
# x variable is containg ord which converts a single Unicode character to its integer equivalent and used to ord the string and add the ord  the key 
# used % 95 and +32 to accepts space and special characters 
    x = (ord(string[i]) +ord(key[i])-32)%95 +32
# chr is return the value from x variable that is represnted in ascii code and it represents back the ascii code to characters in x variable and it adds to encrypt_text   
    encrypt_text += chr(x) 
# calling the encrypt_text variable
  return("" . join(encrypt_text))
# printing the output in encryption function 
print(encryption(x,key))

# defining a function decryption and naming two arguments 
def decryption(encrypt_text, key): 
  orig_text = ''
# using for loop in the range of the length in y variable
  for i in range(len(y)): 
# x variable is containg ord which converts a single Unicode character to its integer equivalent and used to ord the string and subtracting the ord  the key 
# used % 95 and +32 to accepts space and special characters 
    x = (ord(encrypt_text[i]) -ord(key[i]) -32) %95 +32 
#chr is return the value from x variable that is represnted in ascii code and it represents back the ascii code to characters in x variable and it adds to orig_text
    orig_text += chr(x)
# calling the orig_text variable
  return("" . join(orig_text))

# putting the ecryption using x and key arguments
y = encryption(x,key)
# open file 1 and write the encryption
file1 = open("cipher","w")
# write only the encryption
file1.write(y)
# putting the decryption using y and key arguments
z = decryption(y,key) 
print(decryption(y,key))
# open file 3 and write the decryption
file3 = open("decrypt","w")
# write only the decryption
file3.write(z)
# open file 2 and write the key
file2 =open("key","w")
# write only the key 
file2.write(key)

# closing file 1
file1.close()
# closing file 2
file2.close()
# closing file 3
file3.close()



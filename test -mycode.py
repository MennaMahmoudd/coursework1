# Using Python, show how unittest works,so used import unittest to
import unittest
# import main file that includes all codes
import main
# putting the encryption function in testencrypt variable 
testencrypt =main.encryption(main.plaintext,main.key)
# define a class called testmycode that inherits from the TestCase class of the unittest module:
class testmycode(unittest.TestCase):
# define a function 
    def test_encrypt(self):
#using asserequal function to check the equality of the two values comparing the first value which is the  encrypted value equals to value from the testencrypt  and third parameters if the fisrt two values not equal will appear the message 
        self.assertEqual(main.encryption(main.plaintext,main.key),testencrypt,"failed to encrypt")

# putting the decryption function in testdecrypt variable
testdecrypt =main.decryption(main.y,main.key)
# define a class called testmycode that inherits from the TestCase class of the unittest module:
class testmycode(unittest.TestCase):
# define a function
    def test_decrypt(self):
#using asserequal function to check the equality of the two values comparing the first value which is the decrypted value equals to value from the testdecrypt  and third parameters if the fisrt two values not equal will appear the message 
        self.assertEqual(main.decryption(main.y,main.key),testdecrypt,"failed to decrypt")



   
if __name__=="__main__":
    unittest.main()
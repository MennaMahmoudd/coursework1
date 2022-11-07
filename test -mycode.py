import unittest
import main
testencrypt =main.encryption(main.plaintext,main.key)
class testmycode(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(main.encryption(main.plaintext,main.key),testencrypt,"failed to encrypt")


testdecrypt =main.decryption(main.y,main.key)
def test_decrypt(self):
        self.assertEqual(main.decrption(main.y,main.key),testdecrypt,"failed to decrypt")


        
        
if __name__=="__main__":
    unittest.main()
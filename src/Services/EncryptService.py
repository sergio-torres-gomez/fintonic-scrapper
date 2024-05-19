from cryptography.fernet import Fernet

class EncryptService:

    def encrypt(self, key, plain_text):
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(plain_text)

        return cipher_text
    
    
    def decrypt(self, key, cipher_text):
        cipher_suite = Fernet(key)
        plain_text = cipher_suite.decrypt(cipher_text).decode("utf-8")

        return plain_text
    
    def generateKey(self):
        return Fernet.generate_key()
import os
from dotenv import load_dotenv
from src.Services.AWSService import AWSService
from src.Services.EncryptService import EncryptService

class AuthService:

    KEY_FILE = None
    ENC_FILE = None

    USERNAME = None
    PASSWORD = None

    def __init__(self):
        load_dotenv()
        self.KEY_FILE = os.getenv("KEY_FILE")
        self.ENC_FILE = os.getenv("ENC_FILE")
        
        self.__loadAuthFile()

    def __loadAuthFile(self):
        aws = AWSService()

        key = aws.downloadText(self.KEY_FILE)
        cipher_account = aws.downloadText(self.ENC_FILE)

        plain_text = EncryptService().decrypt(key=key, cipher_text=cipher_account)

        self.USERNAME = plain_text.split("|")[0]
        self.PASSWORD = plain_text.split("|")[1]

    def getUsername(self):
        if self.USERNAME is None:
            self.__loadAuthFile()

        return self.USERNAME

    def getPassword(self):
        if self.PASSWORD is None:
            self.__loadAuthFile()

        return self.PASSWORD

    def changeUsernameAndPassword(self, PLAIN_ACCOUNT):
        aws = AWSService()
        encrypt = EncryptService()
        # Generar y guardar una clave de cifrado
        key = encrypt.generateKey()

        # Subir a S3 el archivo de cifrado
        aws.uploadText(text=key, file_name=self.KEY_FILE)

        # Cifrar datos
        encrypt_text = encrypt.encrypt(key=key, plain_text=PLAIN_ACCOUNT)

        # Subir a S3 el archivo cifrado
        aws.uploadText(text=encrypt_text, file_name=self.ENC_FILE)
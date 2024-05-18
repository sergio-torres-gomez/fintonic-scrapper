import boto3
import os
from dotenv import load_dotenv

class AWSService:
    def __init__(self, bucket_name, file_name, session_file):
        load_dotenv()
        self.AWS_ACCESS_KEY = os.getenv("AWS_S3_ACCESS_KEY")
        self.AWS_SECRET_KEY = os.getenv("AWS_S3_SECRET_KEY")
        self.SESSION_FILE = session_file

        self.bucket_name = bucket_name
        self.file_name = file_name
        self.s3 = boto3.client('s3', aws_access_key_id=self.AWS_ACCESS_KEY, aws_secret_access_key=self.AWS_SECRET_KEY)

    def downloadFile(self):
        try:
            self.s3.download_file(self.bucket_name, self.file_name, self.SESSION_FILE)
            print(f"Archivo {self.file_name} descargado")
        except:
            print("Archivo no encontrado en S3")

    def uploadFile(self):
        try:
            # Subir archivo a S3
            self.s3.upload_file(self.SESSION_FILE, self.bucket_name, self.file_name)
            print(f"Archivo {self.SESSION_FILE} subido a {self.bucket_name}/{self.file_name}")
        except FileNotFoundError:
            print(f"El archivo {self.SESSION_FILE} no fue encontrado")
        except:
            print("Error desconocido al subir el archivo")
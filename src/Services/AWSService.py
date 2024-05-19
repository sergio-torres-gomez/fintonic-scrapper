import boto3
import os
from dotenv import load_dotenv

class AWSService:
    def __init__(self):
        load_dotenv()
        self.AWS_ACCESS_KEY = os.getenv("AWS_S3_ACCESS_KEY")
        self.AWS_SECRET_KEY = os.getenv("AWS_S3_SECRET_KEY")
        self.SESSION_FILE = os.getenv("SESSION_FILE")

        self.bucket_name = os.getenv("AWS_S3_BUCKET_NAME")
        self.file_name = os.getenv("AWS_S3_FILE_NAME")
        self.s3 = boto3.client('s3', aws_access_key_id=self.AWS_ACCESS_KEY, aws_secret_access_key=self.AWS_SECRET_KEY)

    def downloadSessionFile(self):
        try:
            self.s3.download_file(self.bucket_name, self.file_name, self.SESSION_FILE)
            print(f"Archivo {self.file_name} descargado")
        except:
            print("Archivo no encontrado en S3")

    def uploadSessionFile(self):
        try:
            # Subir archivo a S3
            self.s3.upload_file(self.SESSION_FILE, self.bucket_name, self.file_name)
        except FileNotFoundError:
            print(f"El archivo {self.SESSION_FILE} no fue encontrado")
        except:
            print("Error desconocido al subir el archivo")

    def uploadText(self, text, file_name):
        try:
            # Subir archivo a S3
            self.s3.put_object(Body=text, Bucket=self.bucket_name, Key=file_name)
            print(f"Archivo {file_name} subido a {self.bucket_name}/{file_name}")
        except FileNotFoundError:
            print(f"El archivo {file_name} no fue encontrado")
        except:
            print("Error desconocido al subir el archivo")

    def downloadText(self, file_name):
        try:
            # Obtener archivo de S3
            response = self.s3.get_object(Bucket=self.bucket_name, Key=file_name)

            return response['Body'].read().decode('utf-8')
        
        except FileNotFoundError:
            print(f"El archivo {file_name} no fue encontrado")
        except:
            print("Error desconocido al recuperar el archivo")
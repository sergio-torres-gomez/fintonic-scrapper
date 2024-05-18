import os
from dotenv import load_dotenv
from src.AWSService import *
from src.FintonicService import *
import requests

### AWS SESSION

load_dotenv()

AWSService = AWSService(
    bucket_name=os.getenv("AWS_S3_BUCKET_NAME"),
    file_name=os.getenv("AWS_S3_FILE_NAME"),
    session_file=os.getenv("SESSION_FILE")
)

AWSService.downloadFile()

fintonicService = FintonicService(AWSService)
listings = fintonicService.getListings()


### IMPORT DATA

url = "http://localhost:8000/api/sync"

payload=listings
headers = {'Content-type': 'application/json'}

try:
    response = requests.request("POST", url, headers=headers, json=payload)
except:
    print("Error connecting to import data API. URL: "+url)

print(response.text)

exit_application("Process finished")

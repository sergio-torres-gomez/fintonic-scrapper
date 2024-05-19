import os
from dotenv import load_dotenv
from src.Services.AWSService import AWSService
from src.Services.FintonicService import FintonicService
import requests
from src.functions import exit_application

### AWS SESSION
aws = AWSService()

aws.downloadSessionFile()

fintonicService = FintonicService()
listings = fintonicService.getListings()


### IMPORT DATA
load_dotenv()
url = os.getenv("SYNC_API_ENDPOINT")

payload=listings
headers = {'Content-type': 'application/json'}

try:
    response = requests.request("POST", url, headers=headers, json=payload)
except:
    print("Error connecting to import data API. URL: "+url)

print(response.text)

exit_application("Process finished")

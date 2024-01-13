from src.FintonicService import *

fintonicService = FintonicService()
listings = fintonicService.getListings()

import requests

url = "http://localhost:8000/api/sync"

payload=listings
headers = {'Content-type': 'application/json'}

try:
    response = requests.request("POST", url, headers=headers, json=payload)
except:
    print("Error connecting to import data API. URL: "+url)
    exit()

print(response.text)

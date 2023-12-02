from src.FintonicService import *

fintonicService = FintonicService()
listings = fintonicService.getListings()
#print(listings)



import requests

url = "http://localhost:8000/api/sync"

payload=listings
headers = {'Content-type': 'application/json'}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.text)

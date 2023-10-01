from src.playwright.Listing import *

class FintonicService:

    LISTING_URL = "https://api.fintonic.com/finapi/rest/transaction/list"
    PARAMS = {
        "pageLimit": 0,
        "pageOffset": 0,
        "read": "false"
    }
    HEADERS = {
        "authority": "api.fintonic.com",
        "accept": "application/vnd.fintonic-v7+json",
        "accept-language": "es-ES,es;q=0.9,en;q=0.8",
        "authorization": "",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "psd2_support": "true",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
    }

    def getListings(self):
        print("Getting listings information.")
        listing = Listing(listing_url=self.LISTING_URL, params=self.PARAMS, headers=self.HEADERS)
        return listing.getListings()
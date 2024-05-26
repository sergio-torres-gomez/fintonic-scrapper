from src.playwright.Listing import *
from src.Services.ApiService import ApiService
from playwright.sync_api import sync_playwright

class FintonicService:

    LISTING_URL = "https://api.fintonic.com/finapi/rest/transaction/list"
    PARAMS = {
        "pageLimit": 0,
        "pageOffset": 0,
        "read": "true"
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

    def __isLoggedInFintonic(self, page):
        auth = Auth(page)
        isLoggedIn = auth.checkIfUserIsLoggedIn()

        if isLoggedIn:
            self.HEADERS["authorization"] = "Bearer "+auth.getBearerToken()
        
        return isLoggedIn

    def getListings(self):
        print("Getting listings information.")

        with sync_playwright() as p:
            page = playwright.initPage(p)
            isLoggedIn = self.__isLoggedInFintonic(page)

            listing = Listing(
                listing_url=self.LISTING_URL, 
                params=self.PARAMS, 
                headers=self.HEADERS,
                page=page,
            )
            
            if isLoggedIn is False:
                listing.login()

            return listing.getListings()
    
    def isLoggedInInApiOrExit(self):
        print("Checking if user is logged in API.")

        apiService = ApiService()
        response = apiService.getLastSession()

        if 'isLoggedIn' in response and response['isLoggedIn']:
            return

        exit_application("User is not logged in.")
    
    def loginFintonic(self):
        print("Logging in Fintonic.")

        with sync_playwright() as p:
            page = playwright.initPage(p)
            listing = Listing(
                listing_url=self.LISTING_URL, 
                params=self.PARAMS, 
                headers=self.HEADERS,
                page=page,
            )
            
            if self.__isLoggedInFintonic(page) is False:
                listing.login()
            
            exit_application("User is logged in.")
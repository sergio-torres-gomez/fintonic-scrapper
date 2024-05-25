from src.playwright.includes.Auth import *
from src.functions import exit_application

class Listing:

    LISTING_URL = None
    _params = {}
    _headers = {
        'accept': 'application/vnd.fintonic-v7+json',
        'authorization': False,
    }
    _session = None

    def __init__(self, listing_url, params, headers, page):
        self.LISTING_URL = listing_url
        self._params = params
        self._headers = headers
        self._session = Auth(page)        
    
    def login(self):
        self._headers["authorization"] = "Bearer "+self._session.login()

    def getListings(self):
        if self._session._page is not None:
            try:
                response = self._session._page.context.request.get(
                    url= self.LISTING_URL,
                    params=self._params,
                    headers=self._headers,
                )

                assert response.ok
            except:
                exit_application("There was error getting Listing. Check USERNAME and PASSWORD parameters.")

            return response.json()

        exit_application("No found current page getting listing information.")
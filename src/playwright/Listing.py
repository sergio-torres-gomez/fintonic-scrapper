from playwright.sync_api import sync_playwright
from src.playwright.includes.Auth import *
import src.playwright.includes.PlaywrightContext as playwright

class Listing:

    LISTING_URL = ""
    _params = {}
    _headers = {}

    def __init__(self, listing_url, params, headers):
        self.LISTING_URL = listing_url
        self._params = params
        self._headers = headers

    def getListings(self):
        with sync_playwright() as p:
            page = playwright.initPage(p)
            session = Auth(page)
            session.login(session_file=playwright.SESSION_FILE)

            if session._bearer != "":
                self._headers["authorization"] = "Bearer "+session._bearer
            else:
                print("There was error getting auth token.")
                exit()

            if session._page is not None:
                
                response = session._page.context.request.get(
                    url= self.LISTING_URL,
                    params=self._params,
                    headers=self._headers,
                )

                assert response.ok

                return response.json()
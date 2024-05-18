from playwright.sync_api import sync_playwright
from src.playwright.includes.Auth import *
import src.playwright.includes.PlaywrightContext as playwright
from src.functions import exit_application
import os
from dotenv import load_dotenv

class Listing:

    LISTING_URL = ""
    _params = {}
    _headers = {}

    def __init__(self, listing_url, params, headers, AWSService):
        self.LISTING_URL = listing_url
        self._params = params
        self._headers = headers
        self.AWSService = AWSService

    def getListings(self):
        load_dotenv()
        SESSION_FILE = os.getenv("SESSION_FILE")
        with sync_playwright() as p:
            page = playwright.initPage(p)
            session = Auth(page)
            session.login(session_file=SESSION_FILE)

            if session._bearer != "":
                self._headers["authorization"] = "Bearer "+session._bearer
            else:
                exit_application("There was error getting auth token.")

            playwright.uploadContext(self.AWSService)

            if session._page is not None:
                try:
                    response = session._page.context.request.get(
                        url= self.LISTING_URL,
                        params=self._params,
                        headers=self._headers,
                    )

                    assert response.ok
                except:
                    exit_application("There was error getting Listing. Check USERNAME and PASSWORD parameters.")

                return response.json()
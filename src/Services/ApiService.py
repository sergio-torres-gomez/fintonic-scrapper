import os
from dotenv import load_dotenv
import requests
from src.functions import exit_application
from datetime import datetime, timedelta

class ApiService:

    IMPORT_MOVEMENTS_URL = None
    LAST_SESSION_API_URL = None
    GET_2FA_CODE_URL = None
    SET_2FA_CODE_PETITION_URL = None

    def __init__(self):
        load_dotenv()
        self.IMPORT_MOVEMENTS_URL = os.getenv("SYNC_API_ENDPOINT")
        self.LAST_SESSION_API_URL = os.getenv("LAST_SESSION_API_URL")
        self.GET_2FA_CODE_URL = os.getenv("GET_2FA_CODE_URL")
        self.SET_2FA_CODE_PETITION_URL = os.getenv("SET_2FA_CODE_PETITION_URL")

    def __doPostJson(self, url, payload):
        headers = {'Content-type': 'application/json'}
        response = requests.request("POST", url, headers=headers, json=payload)

        return response
    
    def __doGetJson(self, url):
        headers = {'Content-type': 'application/json'}
        response = requests.request("GET", url, headers=headers)

        return response.json()

    def importMovements(self, listings):
        url = self.IMPORT_MOVEMENTS_URL

        try:
            return self.__doPostJson(url, listings)
        except:
            exit_application("Error connecting to import data API. URL: " + url)

    def getLastSession(self):
        url = self.LAST_SESSION_API_URL

        try:
            return self.__doGetJson(url)
        except:
            exit_application("Error connecting to API trying to get last session. URL: " + url)

    def getVerificationCode(self):
        url = self.GET_2FA_CODE_URL

        try:
            return self.__doGetJson(url)
        except:
            exit_application("Error connecting to API trying to get verification code. URL: " + url)

    def sent2FACodePetitionToApi(self, timeTo2FA):
        print("Sending 2FA code...")
        url = self.SET_2FA_CODE_PETITION_URL
        sentDate = datetime.now()
        expirationDate = datetime.now() + timedelta(seconds=timeTo2FA)

        new2FAPetition = {
            "isLoggedIn": False,
            "isSmsSent": True,
            "smsSentDate": sentDate.strftime("%Y-%m-%d %H:%M:%S"),
            "smsExpirationDate": expirationDate.strftime("%Y-%m-%d %H:%M:%S")
        }

        try:
            return self.__doPostJson(url, new2FAPetition)
        except:
            exit_application("Error connecting to API trying to sent 2FA code petition. URL: " + url)
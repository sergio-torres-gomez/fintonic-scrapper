import time
import os

# Metaclase para convertir la clase en Singleton
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Auth(object, metaclass=SingletonMeta):

    LOGIN_URL = "https://www.fintonic.com/private/login"
    VERIFY_URL = "https://www.fintonic.com/private/verify"
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")

    _headers = {
        'accept': 'application/vnd.fintonic-v7+json',
        'authorization': False,
    }

    _cookies = {}
    _page = None
    _deviceUuid = ""
    _bearer = ""

    def __init__(self, page):
        self._page = page

    def __closeCookies(self):
        if self._page is not None:
            closeButton = self._page.query_selector("#CybotCookiebotDialogBodyButtonAccept")
            if closeButton != None:
                self._page.click("#CybotCookiebotDialogBodyButtonAccept")

    def __verificateDevice(self):
        if self._page is not None:
            verificationCode = input("Enter Verification Code recibed by sms:")
            try:
                self._page.fill('.MuiInput-input', verificationCode)
                self._page.click('.MuiButton-containedPrimary')
                time.sleep(3)
            except:
                print("There was an error verificating device.")
                exit()

    def __saveBearerToken(self):
        if self._page is not None:
            for cookie in self._page.context.cookies():
                if cookie["name"] == "tk":
                    self._bearer = cookie["value"]
    
    def __saveContext(self, session_file):
        if self._page is not None:
            self._page.context.storage_state(path=session_file)

    def login(self, session_file):
        if self.USERNAME is None or self.PASSWORD is None:
            print("Fill USERNAME and PASSWORD parameters in .env file.")
            exit()
        if self._page is not None:
            self._page.goto(self.LOGIN_URL)
            self.__closeCookies()
            # ingresar las credenciales de inicio de sesión
            isLoggedIn = self._page.url != self.LOGIN_URL
            if not isLoggedIn:
                userIntrduced = self._page.query_selector('#usernameForm') == None
                print("Logging...")
                if not userIntrduced:
                    self._page.fill('#usernameForm', self.USERNAME)
                    self._page.click('#loginButton')
                    time.sleep(3)
                self._page.fill('#password0', [*self.PASSWORD][0])
                self._page.fill('#password1', [*self.PASSWORD][1])
                self._page.fill('#password2', [*self.PASSWORD][2])
                self._page.fill('#password3', [*self.PASSWORD][3])
                self._page.click('#passwordButton')
            else:
                print("User is already logged in.")

            time.sleep(5)
            
            self.__saveBearerToken()

            doubleVerification = self._page.url == self.VERIFY_URL
            if doubleVerification:
                self.__verificateDevice()
            
            self.__saveContext(session_file=session_file)
        else:
            print("There was an error with sync_playwright")
            exit()
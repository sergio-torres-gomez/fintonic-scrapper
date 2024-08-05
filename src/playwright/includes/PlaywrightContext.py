import os
from dotenv import load_dotenv
from src.Services.AWSService import AWSService

TIMEOUT = 120000

def initPage(p):
    load_dotenv()
    SESSION_FILE = os.getenv("SESSION_FILE")
    DEBUG = os.getenv("DEBUG") == "True"
    if DEBUG:
        browser = p.chromium.launch(headless=True, args=["--single-process", "--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"])
    else:
        browser = p.chromium.launch(headless=True, args=["--single-process", "--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"])

    context = getContext(browser, SESSION_FILE)
    page = context.new_page()
    page.set_default_timeout(TIMEOUT)
    page.context.storage_state(path=SESSION_FILE)
    return page 

def getContext(browser, SESSION_FILE):
    try:
        context = browser.new_context(storage_state=SESSION_FILE)
    except FileNotFoundError:
        print("Making state file for session")
        open(SESSION_FILE,'w+')
        with open(SESSION_FILE, 'w') as file:
            file.write("{}")
        os.chmod(SESSION_FILE, 0o777)
        context = browser.new_context(storage_state=SESSION_FILE)
    
    return context

def uploadContext():
    aws = AWSService()
    aws.uploadSessionFile()
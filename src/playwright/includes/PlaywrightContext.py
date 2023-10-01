import os

SESSION_FILE = '/tmp/state.json'

def initPage(p):
    browser = p.chromium.launch()
    context = getContext(browser)
    page = context.new_page()
    page.context.storage_state(path=SESSION_FILE)
    return page 

def getContext(browser):
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
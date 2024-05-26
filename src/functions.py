import os
from dotenv import load_dotenv

def exit_application(msg):
    load_dotenv()
    print(msg)
    # Remove session file
    if os.path.exists(os.getenv("SESSION_FILE")):
        os.remove(os.getenv("SESSION_FILE"))
    exit()
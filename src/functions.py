import os
from dotenv import load_dotenv

def exit_application(msg):
    load_dotenv()
    print(msg)
    # Remove session file
    os.remove(os.getenv("SESSION_FILE"))
    exit()
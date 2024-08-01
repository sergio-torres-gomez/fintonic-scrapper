import os
from dotenv import load_dotenv
from src.Exeptions.ExitApplicationException import ExitApplicationException

def exit_application(msg):
    load_dotenv()
    # Remove session file
    if os.path.exists(os.getenv("SESSION_FILE")):
        os.remove(os.getenv("SESSION_FILE"))
    
    raise ExitApplicationException(msg)
import sys
from src.Services.AuthService import AuthService

args = sys.argv

if len(args) != 3:
    print("Usage: change_fintonic_account.py <username> <password>")
    sys.exit(1)

username = args[1]
password = args[2]

PLAIN_ACCOUNT = "|".join([username, password]).encode('utf-8')

auth = AuthService()
auth.changeUsernameAndPassword(PLAIN_ACCOUNT)

print("Accesos cambiados correctamente.")
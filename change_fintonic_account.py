import sys
from src.Services.AuthService import AuthService

args = sys.argv

if len(args) != 3:
    print("Usage: change_fintonic_account.py <username> <password>")
    sys.exit(1)

username = args[1]
password = args[2]

auth = AuthService()
auth.changeUsernameAndPassword(username, password)

print("Accesos cambiados correctamente.")
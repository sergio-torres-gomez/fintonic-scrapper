from src.Services.AWSService import AWSService
from src.Services.FintonicService import FintonicService
from src.Services.ApiService import ApiService
from src.functions import exit_application



fintonicService = FintonicService()
### CHECK IF FINTONIC SESSION IS LOGGED IN IN API
fintonicService.isLoggedInInApiOrExit()

### AWS SESSION
aws = AWSService()
aws.downloadSessionFile()

listings = fintonicService.getListings()


### IMPORT DATA

apiService = ApiService()
response = apiService.importMovements(listings)

print(response.text)

exit_application("Process finished")

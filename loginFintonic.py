from src.Services.AWSService import AWSService
from src.Services.FintonicService import FintonicService


### AWS SESSION
aws = AWSService()
aws.downloadSessionFile()

fintonicService = FintonicService()
fintonicService.loginFintonic()
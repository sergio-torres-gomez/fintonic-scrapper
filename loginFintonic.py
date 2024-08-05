from src.Services.AWSService import AWSService
from src.Services.FintonicService import FintonicService
import json
from src.Exeptions.ExitApplicationException import ExitApplicationException
from src.Services.ApiService import ApiService


def lambda_handler(event, context):
    try:
        ### AWS SESSION
        aws = AWSService()
        aws.downloadSessionFile()

        fintonicService = FintonicService()
        fintonicService.loginFintonic()

        apiService = ApiService()
        apiService.setApiAsLoggedIn()

        return {
            'statusCode': 200,
            'body': json.dumps(f"Logged in successfully.")
        }
    except ExitApplicationException as e:
        print(f"End of application: {e}")
        
        return {
            'statusCode': 500,
            'body': json.dumps(f"The application has ended: {e}")
        }
    except Exception as e:
        print(f"Unknown error occurred: {e}")
        
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error occurred: {e}")
        }
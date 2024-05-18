# fintonic-scrapper
## How to use:
### First of all, prepare .env file
  
    USERNAME=your_fintonic_username
    PASSWORD=your_fintonic_password
    #Enable for debug mode
    #DEBUG=True

    # FILE FOR SAVE LOGIN SESSION
    SESSION_FILE=path/to/session_file.json

    AWS_S3_BUCKET_NAME=bucket_name
    AWS_S3_FILE_NAME=session_file_name.json
    AWS_S3_ACCESS_KEY=s3_access_key
    AWS_S3_SECRET_KEY=s3_secret_key

### Executing script
  
    python3 sync.py
  

##### Note:
  The first time using application, fintonic will require a sms verfication code. The system will request it if is necesary.
  


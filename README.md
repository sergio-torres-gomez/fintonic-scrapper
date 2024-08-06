# fintonic-scrapper
## How to use:
### First of all, prepare .env file
    #Enable for debug mode
    #DEBUG=True

    # FILE FOR SAVE LOGIN SESSION
    SESSION_FILE=path/to/session_file.json

    AWS_S3_BUCKET_NAME=bucket_name
    AWS_S3_FILE_NAME=session_file_name.json
    AWS_S3_ACCESS_KEY=s3_access_key
    AWS_S3_SECRET_KEY=s3_secret_key

    KEY_FILE=name_key_file
    ENC_FILE=name_encripted_file

    SYNC_API_ENDPOINT=endpoint_url_to_api_sync_movements
    LAST_SESSION_API_URL=endpoint_url_to_api_last_session
    GET_2FA_CODE_URL=endpoint_url_to_api_get_2fa_code
    SET_2FA_CODE_PETITION_URL=endpoint_url_to_api_set_2fa_code

### Executing script
  
    python3 sync.py

### Crontab for automatic sync

  First of all sync.sh must have execution permission.

    0 */2 * * *  /usr/src/scrapper/sync.sh >> /var/log/cron.log 2>&1
  

##### Note:
  The first time using application, fintonic will require a sms verfication code. The system will request it if is necesary.
  


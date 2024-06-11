FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

WORKDIR /usr/src

COPY . .

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install-deps
RUN playwright install 

CMD ["python3", "loginFintonic.py"]
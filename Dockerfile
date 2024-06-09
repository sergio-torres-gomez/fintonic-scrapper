FROM python:3.12

WORKDIR /usr/src

COPY . .

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install 
RUN playwright install-deps

CMD ["python3", "loginFintonic.py"]
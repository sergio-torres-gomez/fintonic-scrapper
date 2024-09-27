## Dockerfile FOR LOGIN IN FROM LAMBDA
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /usr/src

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install-deps
RUN playwright install chromium

# Install the runtime interface client
RUN pip install  \
    --target . \
    awslambdaric

COPY . .

ENTRYPOINT [ "/usr/bin/python", "-m", "awslambdaric" ]
CMD ["loginFintonic.lambda_handler"]
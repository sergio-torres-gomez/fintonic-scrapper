FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /usr/src

COPY . .

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install-deps
RUN playwright install 

# Install the runtime interface client
RUN pip install  \
    --target . \
    awslambdaric


ENTRYPOINT [ "/usr/bin/python", "-m", "awslambdaric" ]
CMD ["loginFintonic.lambda_handler"]
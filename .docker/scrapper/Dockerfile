## Dockerfile FOR SCRAPPER
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /usr/src

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install-deps
RUN playwright install chromium

RUN apt-get update && apt-get install -y cron

RUN chmod +x /usr/src/scrapper/sync.sh

# Create the cron job
COPY crontab.txt /etc/cron.d/cronjobs
RUN chmod 0644 /etc/cron.d/cronjobs
RUN crontab /etc/cron.d/cronjobs

CMD ["cron", "-f"]
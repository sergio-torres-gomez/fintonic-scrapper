#!/bin/bash

# Exportar la variable de entorno PLAYWRIGHT_BROWSERS_PATH
export PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Ejecutar el script de Python
python3 /usr/src/scrapper/sync.py >> /var/log/fintonic_scrapper.log 2>&1
FROM python:3.9

WORKDIR /app

# Copiar los archivos de requerimientos e instalar las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY app /app/app
COPY frameworks /app/frameworks
COPY main.py /app/

# INSTALAR UNA LIBRERIA USANDI PIP
RUN pip install -U https://github.com/iqoptionapi/iqoptionapi/archive/refs/heads/master.zip

CMD ["python", "/app/main.py"]
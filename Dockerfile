
# Creamos una capa a partir de la imagen de python:3.6-slim
FROM python:3.6-slim

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos/descargamos los archivos necesarios para el despliegue de nuesta aplicacion en local
COPY ./src/ /app/src 
COPY ./requirements.txt /app
COPY ./app.py /app
COPY ./status.json /app


# Instalamos las dependencias necesarias indicadas en el archivo requirements-txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Habilitamos el puerto 80 para poder acceder de manera local 
EXPOSE 80


# Lanzamos app.py con los siguientes requisitos
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:__hug_wsgi__"]

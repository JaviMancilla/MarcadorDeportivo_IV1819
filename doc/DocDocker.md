# DOCUMENTACIÓN SOBRE DOCKER

**Docker** es una plataforma para desarrolladores y administradores de sistemas para desarrollar, implementar y ejecutar aplicaciones con contenedores. 

## INSTALACIÓN DE DOCKER Y CREACIÓN DE UN CONTENEDOR.

En este archivo voy a explicar como instalar **Docker** en un entorno Linux como es Ubuntu 18.04. También explicaré como crear un contenedor para cubrir la aplicación a desplegar. 


### 1. Creación de un contenedor.

Para la creación del contenedor **Docker** me ha servido de gran ayuda la documentación de la página oficial de [Docker](https://docs.docker.com/get-started/#docker-concepts).  


Un *contenedor* es una instancia en tiempo de ejecución de una imagen con todo lo necesario para que una o varias aplicaciones se puedan ejecutar. Para que dicho contenedor funcione deberá tener las bibliotecas necesarias para la ejecución, asi como ciertas dependencias, como herramientas del sistema operativo usado. 

Ahora voy explicar como crear un contenedor basandome en la descripción de la pagina oficial de [Docker](https://docs.docker.com/get-started/part2/).

Lo primero que debemos de hacer es definir un fichero denominado **Dockerfile**. Este fichero define lo que sucede en el ambiente dentro del contenedor. 

Para mi aplicación, dicho Dockerfile contiene lo siguiente:

~~~


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


~~~

Una vez creado el archivo *Dockerfile*, estamos listos para su creacíon.

Ubicados en el directorio donde se encuentran los archivos de nuestra aplicación, ejecutamos el siguiente comando:

`docker build -t marcadordeportivo .`

Este comando es el encargado de descargar las dependencias necesarias para nuestra aplicación y de empaquetar el contenido en el contenedor. 

Cuando se haya construido, podemos ejecutar nuestra aplicación de forma local con el siguiente comando:

`docker run -p 5000:80 marcadordeportivo .`

El parametro *-p* es para especifcarle a Docker por el puerto que debe escuchar. 

Dicha orden muestra la siguiente salida:

![runMarcador](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/runMarcador.png?raw=true)

Por último, en nuestro navegador podemos comprobar que la aplicación esta corriendo escribiendo la siguiente url: `0.0.0.0:5000`. 

En mi caso, se muestra es archivo JSON que tengo para pruebas: 

![pruebaMarcador](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/pruebaMarcador.png?raw=true)



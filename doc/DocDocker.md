# DOCUMENTACIÓN SOBRE DOCKER

**Docker** es una plataforma para desarrolladores y administradores de sistemas para desarrollar, implementar y ejecutar aplicaciones con contenedores. 

## INSTALACIÓN DE DOCKER Y CREACIÓN DE UN CONTENEDOR.

En este archivo voy a explicar como instalar **Docker** en un entorno Linux como es Ubuntu 18.04. También explicaré como crear un contenedor para cubrir la aplicación a desplegar. 



### 1. Instalación de Docker.

Para la instalación de **Docker** me ha servido de ayuda la documentación de la página oficial de [Docker](https://docs.docker.com/get-started/#docker-concepts) y este [tutorial](https://ubunlog.com/como-instalar-docker-en-ubuntu-18-04-y-derivados/) sobre aplicaciones en Linux. 

Por lo tanto, aquí explicaré como he podido realizar dicha instalación de manera mas resumida. Para profundizar más se pueden consultar los enlaces mencionados anteriormente. 

En primer lugar, antes de ponernos a instalar cualquier versión, nos aseguramos de que no tenemos ninguna versión anterior a **Docker** para poder hacer una instalación limpia. Entonces ejecutamos el siguiente comando:

` sudo apt-get remove docker docker-engine docker.io`

Después, debemos actualizar nuestros repositorios asi como cualquier paquete vinculado con el sistema:

` sudo apt-get update`

` sudo apt-get upgrade`


Una vez hecho esto, podemos comenzar con la instalación de **Docker**.

Lo primero, instalar algunas dependencias necesarias para Docker con los siguientes comandos:

~~~

sudo apt-get install \
 
apt-transport-https \
 
ca-certificates \
 
curl \
 
software-properties-common

~~~


Una vez instaladas dichas dependecias, ya podemos realizar la instalación de Docker en nuestro sistema. Ejecutamos el siguiente comando:

` sudo apt-get install docker-ce`

Para verificar que Docker a tenido una instalación correcta y que se esta ejecutando sin problemas, podemos realizar una prueba ejecutando el siguiente comando: 

` sudo docker run hello-world `

El resultado, si es correcta la instalación, será similar al de la siguiente imagen: 

![rundocker](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/runDocker.png?raw=true)



### 2. Creación de un contenedor.

Un *contenedor* es una instancia en tiempo de ejecución de una imagen con todo lo necesario para que una o varias aplicaciones se puedan ejecutar. Para que dicho contenedor funcione deberá tener las bibliotecas necesarias para la ejecución, asi como ciertas dependencias, como herramientas del sistema operativo usado. 

Ahora voy explicar como crear un contenedor basandome en la descripción de la pagina oficial de [Docker](https://docs.docker.com/get-started/part2/).

Lo primero que debemos de hacer es definir un fichero denominado **Dockerfile**. Este fichero define lo que sucede en el ambiente dentro del contenedor. 

Para mi aplicación, dicho Dockerfile contiene lo siguiente:

~~~

# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80


# Run app.py when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:__hug_wsgi__"]

~~~

Este ficher contiene las siguientes instrucciones:
 - **FROM**: crea una capa partir la imagen de `python:3.6-slim` de Docker.
 - **WORKDIR**: establce el directorio de trabajo.
 - **COPY**: agrega archivos desde el directorio actual del cliente.
 - **RUN**: construye la aplicación, en este caso atraves del comando definido con sus respectivas dependencias incluidas en el requirements.txt
 - **EXPOSE**: especifica que puerto ha de estar habilitado. 
 - **CMD**: especifica que comando se ejecuta dentro del contenedor. En esta caso necesita *gunicorn*, el puerto donde escucha y el parametro de la app. 


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



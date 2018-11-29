# DOCUMENTACIÓN SOBRE DESPLIEGUE DEL CONTENEDOR EN HEROKU.

Para la realización de este apartado, me ha sido de gran utilidad la documentación que aporta **Heroku** para este tema. Dicha documentación se puede encontrar en la página oficial de [Heroku](https://devcenter.heroku.com/articles/container-registry-and-runtime)


### 1. DESCARGA DE HEROKU CLI.

Para la descarga e instalación de Heroku CLI podemos consultar la documentación que se hizo para el hito anterior. Dicha documentación se puede encontrar [aqui](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/DespliegueHeroku.md).

### 2. AUTENTIFICACIÓN EN HEROKU.

Debemos de autentificarnos en Heroku pero en el modo de registro de contenedores. Utilizamos el siguiente comando:

` heroku container:login `

### 3. CREACIÓN DEL FICHERO *DOCKERFILE*.

Para el despliegue del contenedor en Heroku, hemos modificado el *Dockerfile* con respecto al del despliegue en local. El contenido del archivo quedará asi: 

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
CMD gunicorn app:__hug_wsgi__ --log-file -

~~~

### 4. CREACIÓN DE LA APLICACION.

Una vez actualizado el archivo *Dockerfile*, pasamos a construir la aplicación en la web de Heroku. En la siguiente imagen especificamos como:

![appHeroku](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/createappHeroku.png?raw=true)

Intruducimos el nombre de nuestra app y la creamos. 

### 5. CONSTRUCCIÓN Y LANZAMIENTO DEL CONTENEDOR.

Para la construcción del contenedor utilizamos el siguiente comando:

` heroku container:push web --app <nombre>`

Dicho nombre es el que le dimos en el punto anterior. 

En la siguiente imagen vemos como he desplegado mi contenedor: 

![buildHeroku](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/heroku-docker-push.png?raw=true)

Al finalizar la construcción, ya solo nos quedará lanzar nuesro contenedor a los registros de Heroku. Usamos el siguiente comando:

` heroku container:release web --app <nombre>`

![releaseHeroku](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/heroku-docker-release.png?raw=true)


Y ahora podemos comprobar que nuestro contenedor esta lanzado con éxito. 

[Heroku Docker](https://marcador-deportivo-docker.herokuapp.com/status)
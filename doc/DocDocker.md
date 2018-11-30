# DOCUMENTACIÓN SOBRE DOCKER

**Docker** es una plataforma para desarrolladores y administradores de sistemas para desarrollar, implementar y ejecutar aplicaciones con contenedores. 

## CREACIÓN DE UN CONTENEDOR CON DOCKER.

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

### 2. Despliegue en local.

Cuando se haya construido, podemos ejecutar nuestra aplicación de forma local con el siguiente comando:

`docker run -p 5000:80 marcadordeportivo .`

El parametro *-p* es para especifcarle a Docker por el puerto que debe escuchar. 

Dicha orden muestra la siguiente salida:

![runMarcador](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/runMarcador.png?raw=true)

Por último, en nuestro navegador podemos comprobar que la aplicación esta corriendo escribiendo la siguiente url: `0.0.0.0:5000`. 

En mi caso, se muestra es archivo JSON que tengo para pruebas: 

![pruebaMarcador](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/pruebaMarcador.png?raw=true)

### 3. Despliegue de nuestro contenedor en Heroku

Para desplegar nuestro conteneder en Heroku, lo primero que hecho ha sido crear una nueva aplicación en la web de Heroku. Dicha aplicación la he nombrado `marcador-deportivo-docker` para poder diferenciarla de la otra, que fue creado en un hito anterior.

Para consultar como crear un aplicación en la web de Heroku podemos consultar el enumerado 2 la siguiente guia: [Despliegue Heroku](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/DespliegueHeroku.md).

Una vez creada la nueva aplicación prodecemos a crear el archivo `heroku.yml`. Para la creación de dicho fichero me he basado en el tutorial que ofrece la propia pagina de Heroku que podemos ver [aquí](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml).

Este archivo tiene con misión difinir una aplicacián en Heroku permitiendo construir imágenes de Docker en Heroku. Por tanto el fichero tiene el siguiente contenido:

~~~

build:
  
  # Aqui especificamos donde va a estar el archivo Dockerfile
  docker:
    web: Dockerfile 
run:

  # Esta seccion es la encargada de ejecutar la app. 
  web: gunicorn app:__hug_wsgi__ --log-file -

~~~


Una vez definido el fichero `heroku.yml`, procedemos a subirlo a nuestro repositorio de GitHub de la manera en la que se subie cualquier archivo.

Debemos de establecer la aplicación creada con anterioridad, `marcador-deportivo-docker` como un contenedor. Para esteblecerla usamos la siguiente orden:

`heroku stack:set container --app marcador-deportivo-docker`

![setContenedor](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/setContenedorHeroku.png?raw=true)

Lo siguiente a hacer es indicar en que repositorio queremos actualizar los datos de nuestra aplicación. Como queremos que en este caso sea en la aplicación creada como contenedor, es decir en `marcador-deportivo-docker` lo especificamos de la siguiente manera:

`heroku git:remote -a marcador-deportivo-docker`


Una vez realizado todo esto, cuando realicemos un cambio en nuestra aplicación y añadamos los cambios a nuestro repositorio, para desplegarla en Heroku usaremos la siguiente orden:

`git push heroku master` 

Hecho estoy podemos comprobar que nuestra aplicación funciona correctamente: [Despliegue Heroku](https://marcador-deportivo-docker.herokuapp.com/)

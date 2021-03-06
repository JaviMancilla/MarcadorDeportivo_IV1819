# MARCADOR DEPORTIVO 

# REPOSITORIO PARA EL PROYECTO DE INFRAESTRUCTURA VIRTUAL (2018)

## Nombre del proyecto: Marcador Deportivo.
## Autor: Javier García Mancilla 

### DESCRIPCIÓN:

   Este repositorio será utilizado para la creación de un servicio web.

   Este servicio web nos informará del calendario de partidos de fútbol tanto para **LaLiga** como para la **Champios League**.

   Nos informará de los partidos de nuestro equipo, dandonos información relativa al rival, fecha y hora del partido y también donde podremos disfrutar de su restransmisión. 


### HERRAMIENTAS:

- **LENGUAJE** .

    El lenguaje a utilizar para la creación del proyecto será [**Python**](https://www.python.org/), ya que es un lenguaje de programación orientado a objetos el cual está a la orden del dia y me atreveria a decir que hoy por hoy es el lenguaje más utilizado.


- **FRAMEWORK**.

    Como framework, optaré por la utilizacion de [**Hug**](http://www.hug.rest/). *Hug* es una API de desarrollo implementada en Python 3. Es un micro-framework, lo que significa que contiene el menor código e integraciones posibles para que sea totalmente funcional, lo que a su vez proporciona un mayor rendimiento. Este framework fue una recomendación de JJMelero, profesor de la asignatura y anfitrión del Hackatón de diseño dirigido por test de microservicios.


- **BASE DE DATOS**.

    Para la creación de la base de datos del proyecto, vamos a utilizar un sistema de gestión de bases de datos como es [**MariaDB**](https://mariadb.org/).


### DESARROLLO DEL PROYECTO:

- **DESCRIPCION DE LA CLASE**

Se ha creado una clase partidos, la cual se encuentra alojada en `/travistes/marcadorDeportivo.py` y crea un objeto partido a partir de los siguientes atributos: id_partido, jornada, equipo_local, equipo_visitante, fecha, hora, lugar, canalTV.

Dicho esto, en `/test/test_marcador.py`, se encuentran alojadas las pruebas que hasta ahora hay creadas. Dichas pruebas nos aseguran de cada uno de los atributos del objeto partido son correctos. 

-------------------------------------------------------------

- **INSTALACIÓN Y TESTEO**

Para su instalación lo primero que debemos de hacer es clonar este repositorio:

`git clone https://github.com/JaviMancilla/MarcadorDeportivo_IV1819.git`

Posteriormente debemos instalar *pytest*, ya que se usará para pruebas unitarias:

`pip install pytest`

Por último, a modo local, para comprobar que todo funciona correctamente o ver si algún test no ha pasado la prueba, desde el directorio `/marcador` ejecutamos el comando `pytest`.  

-------------------------------------------------------------

- **INTEGRACIÓN CONTINUA MEDIANTE TRAVIS**

Tras habernos dado de alta en [**Travis**](https://travis-ci.org) con nuestra cuenta de **github** y sincronizando nuestro proyecto. Los resultados son los siguientes: [![Build Status](https://travis-ci.org/JaviMancilla/MarcadorDeportivo_IV1819.svg?branch=master)](https://travis-ci.org/JaviMancilla/MarcadorDeportivo_IV1819)

-------------------------------------------------------------

- **DESPLIEGUE MEDIANTE HEROKU**

Una vez que nos hayamos registrado en [**Heroku**](https://id.heroku.com/login) y haber realizado los pasos para desplegar nuestra aplicación, podemos ver el resultado del despliegue en el siguiente enlace:

+ [**Despliegue**](https://marcadordeportivo.herokuapp.com/)
+ Configuración del despliegue [**aquí**](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/DespliegueHeroku.md)

-------------------------------------------------------------

- **DESPLIEGUE DE CONTENEDORES CON DOCKER Y HEROKU**

+ Contenedor:[https://marcador-deportivo-docker.herokuapp.com/status](https://marcador-deportivo-docker.herokuapp.com/status)
+ Documentación Docker [aquí](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/DocDocker.md)

+ Enlace a DockerHub: [MarcadorDeportivo-DockerHub](https://hub.docker.com/r/jmanci/marcadordeportivo_iv1819/)
+ Documentación DockerHub [aquí](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/DocDockerHub.md)

-------------------------------------------------------------


- **DESPLIEGUE DESDE 0 DE UNA APLICACIÓN EN LA NUBE**

+ Despliegue final: marcador-deportivo-18-19.westeurope.cloudapp.azure.com
+ Documentacion Despliegue [aquí](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/DocDespliegue0.md)
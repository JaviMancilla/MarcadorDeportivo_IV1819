# DESPLIEGUE EN HEROKU

Para la configuración del despliegue en **Heroku**, hemos seguido los pasos de este tutorial que nos proporciona la propia página de este y que añadimos a continuación:

- [Tutorial](https://devcenter.heroku.com/articles/getting-started-with-python) 

Este tutorial proporcionado por la propia página de Heroku, nos muestra un ejemplo de como desplegar un servicio utilizando el lenguaje **Python**.

A raiz de este ejemplo dejo los pasos a seguir para esta aplicación en concreto:

### PROCEDIMIENTO

1. **Registro en Heroku** 

    Accedemos a la página de **Heroku** y nos registramos. 

    [Heroku Login](https://signup.heroku.com/login?redirect-url=https%3A%2F%2Fid.heroku.com%2Foauth%2Fauthorize%3Fclient_id%3D1e7d4c52-6008-4a73-b132-09abb5d04859%26response_type%3Dcode%26scope%3Dglobal%252Cplatform%26state%3DSFMyNTY.g3QAAAACZAAEZGF0YW0AAAAxaHR0cHM6Ly9kYXNoYm9hcmQuaGVyb2t1LmNvbS9hdXRoL2hlcm9rdS9jYWxsYmFja2QABnNpZ25lZG4GAHcarsRmAQ.0XivXF_mTSVVsQSU5WwWutefChzM46-0W5qoZ7agEhw) 

2. **Creación de la aplicación**

    Una vez finalizado el registro, debemos de instalar **Heroku** en nuestro host para ser usado en linea de comandos. 
    
    Procedemos a instalarlo con los siguientes comandos:

    `sudo snap install heroku --classic`

    Hacemos login desde nuestra terminal,

    `heroku login`

    y escribimos nuestro nombre de usuario y clave correspondiente para poder usar nuestra cuenta a traves de la terminal.

    Y para finalizar creamos nuestra aplicacíon como se muestra en la siguiente imagen: 

    ![Create app](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/createappHeroku.png?raw=true)


3. **Despliegue con GitHub**

    ![Despliegue GitHub](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/herokuGithub.png?raw=true)


4. **Crear archivo Procfile**

    Dicho archivo especifica los comandos que van a ser ejecutados por los términos de la aplicación. Este archivo se usa para declarar una variedad de tipos de proceso, en mi caso, dicho archivo especifica lo siguiente:

    `web: gunicorn app:__hug_wsgi__ --log-file -`

5. **Actualizar el archivo requirements.txt**

    Este archivo contiene una lista de comandos para *pip* que instala las versiones necesarioas de los paquetes dependientes. En esta caso, mi archivo contiene las siguientes dependencias:
    
    ~~~

    atomicwrites==1.2.1
    attrs==18.2.0
    DateTime==4.3
    more-itertools==4.3.0
    pluggy==0.7.1
    py==1.6.0
    pytest==3.8.2
    pytz==2018.5
    six==1.11.0
    zope.interface==4.5.0
    hug
    gunicorn

    ~~~

6. **Comprobar que la aplicación esta desplegada**

    - [Despliegue](https://marcadordeportivo.herokuapp.com/)
# DOCUMENTACIÓN SOBRE DOCKER-HUB

### 1. REGISTRO.

Para poder utilizar **Docker Hub**, antes que nada debemos de crearnos una cuenta [aquí](https://hub.docker.com/).


### 2. SINCRONIZACIÓN CON GIT-HUB.

Una vez creada nuestra cuenta, debemos de sincronizarla con nuestra cuenta de **Git-Hub**. Esto se hace accediendo a *Settings* > *Linked Accounts & Services* y seleccionamos donde aparece Git-Hub. 

![hub1](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hub1.png?raw=true)


### 3. CREACIÓN Y CONFIGURACIÓN DEL DESPLIEGUE AUTOMÁTICO.

Una vez sincronizados con Git-Hub, procedmos a la creación de nuestro despliegue. Para ello vamos a *Create* > *Create Automated Build*. Una vez ahí, seleccionamos *Create Auto-build Git-Hub*. 

Una vez ahí, aparece una lista con nuestros repositorios de asociados a nuestra cuenta y debemos marcar el que nos interese, en mi caso selecciono *MarcadorDeportivo_IV1819*.

![hub3](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hub3.png?raw=true)

En el siguiente paso, aparecen los campos para dicha creación, donde podemos especificar alguna descripción o la visibilidad del mismo. 

![hub4](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hub4.png?raw=true)

Una vez creado, podemos comprobar que ya lo tenemos listo.

![hub5](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hub5.png?raw=true)

Antes de finalizar debemos ir a nuestra cuenta de Git-Hub y comprobar en nuestro repositorio especificado en Docker-Hub que se ha añadido un *Webhook* de Docker. 

![hub6](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hub6.png?raw=true)
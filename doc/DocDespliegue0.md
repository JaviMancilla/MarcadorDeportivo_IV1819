# DESPLIEGUE DESDE 0 DE UNA APLICACIÓN EN LA NUBE

La realización de la tarea de despligue, podriamos dividirla en tres partes. Una parte seria la correspondiente a crear el provisionamiento para el despliegue, creado con la herramiento **Ansible** y que se puede ver mas desarrollado en el Apartado 1; otra parte sería la construcción de una máquina virtual (algunas veces la denotaré como MV) la cuál será desplegada en Azure y mejor detallado en el Apartado 2; y para finalizar habría que automatizar dicho despliguen con el usos de un fichero por medio de la herramienta **Fabric**, Apartado 3. 

## 1. PROVISIONAMIENTO PARA DESARROLLO.

Para el desarrollo del provisionamiento, como he dicho anteriormente he utilizado la herramienta **Ansible**. Dicha herramienta trata la configuración y administración de un computador o máquinas virtuales que será nuestro caso.

Para ello he construido un archivo *playbook* denominado *playbook.yml*, valga la redundancia, el cuál es el lenguaje de configuración, despligue y orquestación que usa **Ansible**. Su uso es describir una política a aplicar sobre un sistema (una máquina virtual en este caso). Para más informacion sobre *playbook* puede verse en [Linuxito](https://www.linuxito.com/gnu-linux/nivel-alto/963-playbooks-en-ansible).

Dicho esto, mostramos el contenido de dicho archivo:

~~~

- hosts: all
  sudo: yes
  remote_user: javimancilla

  tasks:
  - name: Añadir repositorio de python 3.6
    become: true
    apt_repository: repo=ppa:deadsnakes/ppa state=present

  - name: Actualizar sistema
    become: true
    command: sudo apt-get update

  - name: Instalar Python 3.6
    become: true
    apt: pkg=python3.6 state=present

  - name: Cambio version de python
    command: sudo ln -sfn /usr/bin/python3.6 /usr/bin/python

  - name: Instalacion de pip3
    become: true
    command: sudo apt-get -y install python3-pip

  - name: Instalar GitHub
    become: true
    command: sudo apt-get install -y git

  - name: Clonar repositorio de GitHub
    git: repo=https://github.com/JaviMancilla/MarcadorDeportivo_IV1819.git dest=marcadordeportivo/ force=yes

  - name: Instalar Requerimientos
    command: pip3 install -r marcadordeportivo/requirements.txt

~~~

Se observa que solo poseemos un items, que en este caso se para todos los hosts (`hosts:all`). Para este items, se crean varias tareas, que podemos destacar alguna como la de actualizar el sistema o la de la instalación de GitHub por poner algun ejemplo entre las otras que hay. 

Una vez realizado esto y previamente haber instalado **Ansible** en nuestra máquina *host*, debemos de configurar el archivo ubicado en `/etc/ansible/hosts`, para especificar que host van a utilizar este archivo de provisionamiento y debemos de datallar una IP o un nombre de dominio. En mi caso he escrito un nombre de domino. La información aparace tal que así:

~~~

[marcadordeportivo]
marcador-deportivo-18-19.westeurope.cloudapp.azure.com

~~~

Hecho esto, ya tenemos preparado nuestro provisionamiento para la máquina virtual que procedemos a crear y configurar en el siguiente paso. 


## 2. CREACIÓN DE UNA MÁQUINA VIRTUAL.

Posterior a la creación del fichero de provisionamiento, nos disponemos a crear y configurar una máquina virtual de tipo IaaS que se alojará en los servidores de [Azure](https://azure.microsoft.com/es-es/). Para la creación de esta máquina virtual he usado la herramienta [Vagrant](https://www.vagrantup.com/). 

Para el desarrollo de este apartado, me ha servido de gran ayuda [este repositorio](https://github.com/Azure/vagrant-azure) de git donde aparece mucha información relacionada con el tema a tratar. 

A partir aquí, expongo paso a paso como he realizado la creación y prueba de la máquina virtual y del despligue en Azure.

### 2.1. Instalar Azure CLI.

Para iniciar la creación de la maquina virtual, debemos instalar el complemento de Azure **Azure CLI**. Para la instalación de este complemento he consultado la documentación oficial de Azure que podemos encontrar [aquí](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest). 

### 2.2. Login en Azure.

Paso previo a hacer login en Azure, obviamente hay que estar registrados en dicha plataforma. En mi caso he usado una cuenta de tipo educativa, la cuál a sido proporcionada por el profesor titular de la asignatura "Infraestructura Virtual" de la Universidad de Granada.

Una vez registrados en la plataforma, desde una terminal de nuestro ordenador, pondremos el siguiente comando:

`az login` 

Este comando nos redijirá, mediante el navegador, para acceder a nuestra cuenta de Azure. 

![az-login](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hito5/az_login.png?raw=true)

Aquí nos aparecerán los datos asociados a nuestra/s suscripciones actuales de Azure.  


### 2.3. Crear AAD con acceso a Azure Resource Manager.

Con la siguiente orden conseguimos crear un Azure Active Directory con acceso a Azure Resource Manager para la suscripción actual de Azure.

`az ad sp create-for-rbac`

![aad](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hito5/crearAAD.png?raw=true)

### 2.4. Obtener ID de suscripción de Azure.

Si no nos sabemos nuestra ID de suscripción de Azure podemos verla con la siguiente orden. 

`az account list --query "[?isDefault].id" -o tsv`

![idAzure](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hito5/idAzure.png?raw=true)

### 2.5. Exportar varibles de entorno.

Este paso es bastante recomendable a la hora de crear el archivo Vagrantfile, ya que Vagrantfile posee variables de entorno asociadas a Azure que no son del sistema y por tanto no nos las va a reconocer como tales. Por ello la realización de este paso.

Dichas variables hay que identicarlar con los campos asociados a nuestros datos de Azure, tal que asi:

AZURE_TENANT_ID --> asociado al campo "tenant"
AZURE_CLIENT_ID --> asociado al campo "appID"
AZURE_CLIENT_SECRET --> asociado al campo "password"
AZURE_SUBSCRIPTION_ID --> asociado a la ID que obtuvimos en el paso 2.4.

La exportacion de la variables se muestra como ejemplo en la imagen siguiente.

![export](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hito5/Env.png?raw=true)

Lo realizado anteriormente es una recomendación, que bajo mi punto de vista es más seguro, ya que en vez de utilizar variables de entorno en el archivo Vagrantfile, podriamos poner los campos tal cual se describen.


### 2.6. Crear Vagrantfile.

Una vez realizado todo lo anterior procedemos con la construción de nuestro Vagrantfile, nuestro archivo que procederá a construir y a provisionar, con la ayuda del archivo creado en el apartado 1, nuestra máquina virtual que ofreceré el despligue. 

Dicho archivo contiene lo siguiente:

~~~
Vagrant.configure('2') do |config|
  config.vm.box = 'azure'

  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.vm.provider :azure do |azure, override|

    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    # Variables correspondientes a la creacion de la MV
    azure.vm_name = "marcador-deportivo-18-19"
    azure.vm_size = "Standard_D2_v2"
    azure.tcp_endpoints = "80"
    azure.location = "westeurope"
    azure.admin_username = "javimancilla"


  end

  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provision/playbook.yml"
  end

end

~~~

Podemos observar que hay declaradas bastantes variables de Azure, declaradas como variables de entorno, las cuales son la que hablabamos en el apartadado 2.5.

Luego también se observan variables relacionadas con la MV, como el nombre, que se establecerá después como el DNS del MV; el tamaño de la MV; el puerto o la localización de la MV. 

La última función de este archivo especifica que vamos a utilizar un archivo para el provisionamiento y que se ha desarrollado con la herramiento **Ansible**. También se especifica donde se encuentra dicho fichero.



### 2.7. Instalar complemento Vagrant-Azure.

Para continuar con el despligue de la MV, es conveniente instalar otro complemente como es el complemento *vagrant-azure*. Este complemento se usa para poder desplegar con Vagrant una máquina virtual en Azure.

Para ello utilizamos el siguiente comando:

` vagrant plugin install vagrant-azure ` 

![pluginAzure](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hito5/pluginAzure.png?raw=true)


### 2.8. Despliegue.

Para realizar el despliegue utilizamos la siguiente orden:

` vagrant up --provider=azure` 

La máquina virtual se irá creando con las credenciales que le asignamos en nuestro archivo Vagrantfile y con el provisionamiento que explicamos en el apartado 1. 

![despliegue](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hito5/despliegue1.png?raw=true)
![provisionamiento](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hito5/provisionamiento.png?raw=true)

También podemos comprobar que en nuestra cuenta de Azure, en el sitio de máquinas virtuales, se ha creado una máquina virtual.

![despligue_azure](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hito5/azure_mv.png?raw=true)


### 2.9. Comprobación. 

Una vez realizado el despligue, quiero comprobar que se ha hecho correctamente antes de lanzarlo con **Fabric**. Para ello lanzamos la máquina virtual via ssh como aparece en la imagen siguiente:

![vagrantssh](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hito5/vagrantssh.png?raw=true)

Comprobamos las urls correspondientes:

![url](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hito5/url.png?raw=true)
![status](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hito5/status.png?raw=true)

Visto que todo funciona como se esperaba, podemos apagar la máquina virtual.

![vagranthalt](https://github.com/JaviMancilla/MarcadorDeportivo_IV1819/blob/master/doc/img/hito5/apagarvagrant.png?raw=true)


## 3. DESPLIGUE USANDO FABRIC

Para la automatización del despligue se hace necesario construir un archivo python basado en la herramienta **Fabric**. Dicho archivo, denominado *fabfile.py* nos permite usar ordenes de manera automatica a traves de ssh.

La información asociada a **Fabric** ha sido consultada desde [aquí](http://docs.fabfile.org/en/1.14/index.html).

El archivo *fabfile.py* contiene lo siguiente:

~~~

# Importamos el modulo de fabric
from fabric.api import *

def ActualizarServicio():

    # Descartamos la version anterior de la aplicación
    run('rm -rf MarcadorDeportivo_IV1819')

    # Actualizamos a la nueva versión descargando el repositorio
    run('git clone https://github.com/JaviMancilla/MarcadorDeportivo_IV1819.git')

    # Instalamos requirements
    run('pip3 install -r MarcadorDeportivo_IV1819/requirements.txt')


def IniciarServicio():

     # Iniciamos el servicio web
     run('cd MarcadorDeportivo_IV1819/ && sudo gunicorn app:__hug_wsgi__ -b 0.0.0.0:80')

~~~

Podemos observar que he definido una serie de funciones que llevan a cabo diferentes ordenes como para actualizar el servicio o iniciarlo.

Para llevar a cabo alguna de la funcioón especificada en el archivo la orden será la siguiente:

fab -f despliegue/fabfile.py -H vagrant@marcador-deportivo-18-19.westeurope.cloudapp.azure.com "nombre_funcion"


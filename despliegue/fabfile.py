

# Importamos el modulo de fabric
from fabric.api import *

def ActualizarServicio():

    # Descartamos la version anterior de la aplicación
    run('sudo rm -rf MarcadorDeportivo_IV1819')

    # Actualizamos a la nueva versión descargando el repositorio
    run('git clone https://github.com/JaviMancilla/MarcadorDeportivo_IV1819.git')

    # Instalamos requirements
    run('pip3 install -r MarcadorDeportivo_IV1819/requirements.txt')


def IniciarServicio():

     # Iniciamos el servicio web
     run('cd MarcadorDeportivo_IV1819/ && sudo gunicorn app:__hug_wsgi__ -b 0.0.0.0:80')
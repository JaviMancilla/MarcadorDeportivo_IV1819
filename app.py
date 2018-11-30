import hug
import json

from src.marcadorDeportivo import Partido


@hug.get('/')
def prueba():

    resp = {"STATUS":"Ok"}

    return resp


@hug.get('/status')
def status():
    marcador = Partido()
    valor = marcador.status()

    if valor == 'OK':
        with open('status.json') as f:
            respuesta = json.load(f)

    
    return respuesta



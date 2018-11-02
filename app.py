import hug
import json

from travistest.marcadorDeportivo import Partido


@hug.get('/')
def status():
    marcador = Partido()
    valor = marcador.status()

    if valor == 'OK':
        with open('status.json') as f:
            resp = json.load(f)

    
    return resp



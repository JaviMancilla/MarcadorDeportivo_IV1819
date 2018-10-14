import datetime

class Partido:
    def __init__(self, id_partido, jornada, equipo_local, 
                 equipo_visitante, fecha, hora, lugar, canalTV):

        self.id_partido = id_partido
        self.jornada = jornada
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar
        self.canalTV = canalTV

    def comprobar_jornada(self):
        return isinstance(self.jornada, int)

    def comprobar_equipo_local(self):
        return isinstance(self.equipo_local, str)

    def comprobar_equipo_visitante(self):
        return isinstance(self.equipo_visitante, str)

    def comprobar_fecha(self):
        return isinstance(self.fecha, datetime.date)

    def comprobar_hora(self):
        return isinstance(self.hora, datetime.time)

    def comprobar_lugar(self):
        return isinstance(self.lugar, str)

    def comprobar_canalTV(self):
        return isinstance(self.canalTV, str)

    def modificar_equipoLocal(self, equipo_local):
        self.equipo_local = equipo_local

    def modificar_equipoVisitante(self, equipo_visitante):
        self.equipo_visitante = equipo_visitante

    def modificar_fecha(self, fecha):
        self.fecha = fecha

    def modificar_hora(self, hora):
        self.hora = hora

    def modificar_lugar(self, lugar):
        self.lugar = lugar

    def modificar_canal(self, canalTV):
        self.canalTV = canalTV

    def mostrar_partido(self):
        print("Jornada", self.jornada)
        print(self.equipo_local, "vs", self.equipo_visitante)
        print(self.fecha, self.hora)
        print(self.lugar)
        print(self.canalTV)

 
    

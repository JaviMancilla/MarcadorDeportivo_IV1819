import datetime

from pytest import fixture

@fixture

def op():
    from travistest.marcadorDeportivo import Partido
    return Partido(1, 1,"Real Madrid", "Barcelona", datetime.date(2018, 10, 28), datetime.time (18, 00) , "Santiago Bernabeu", "Movistar")

def test_jornada(op):
    assert op.comprobar_jornada()

def test_equipo_local(op):
    assert op.comprobar_equipo_local()

def test_equipo_visitante(op):
    assert op.comprobar_equipo_visitante()
       
def test_fecha(op):
    assert op.comprobar_fecha()

def test_hora(op):
    assert op.comprobar_hora()

def test_lugar(op):
    assert op.comprobar_lugar()

def test_canalTV(op):
    assert op.comprobar_canalTV()
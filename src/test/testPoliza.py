import sys
import os
sys.path.append(os.path.abspath('./core/'))

from usuarioCliente import UsuarioCliente
from poliza import Poliza
from tipoPoliza import TipoPoliza
from moduloExtra import ModuloExtra


from typing import List
import datetime


# Test comparación pólizas
def test_compare_poliza():
	u = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	u2 = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	fecha = datetime.datetime(2020, 5, 17)
	fecha2 = datetime.datetime(2020, 5, 18)
	
	t1 = Poliza(u, "12345678", fecha, TipoPoliza.Basica, 35.99, 103.0, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	t2 = Poliza(u2, "12345678", fecha, TipoPoliza.Basica, 35.99, 103.0, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test

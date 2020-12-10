import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from usuarioCliente import UsuarioCliente
from poliza import Poliza
from tipoPoliza import TipoPoliza
from moduloExtra import ModuloExtra
from typing import List
import datetime

# Test comparación pólizas
def test_compare_poliza():
	# Creación usuario cliente
	u = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678")
	# Creación de fecha
	fecha = datetime.datetime(2020, 5, 17)
	# Creación de dos pólizas idénticas
	t1 = Poliza(u, "12345678", fecha, TipoPoliza.Basica, 35.99, 103.0, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	t2 = Poliza(u, "12345678", fecha, TipoPoliza.Basica, 35.99, 103.0, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	# Creación de una póliza distinta
	t3 = Poliza(u, "12345678", fecha, TipoPoliza.Basica, 35.99, 20.0, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	# Comprobar que una póliza es igual a otra si tienen la misma información
	assert t1 == t2 # Pasa test
	# Comprobar que una póliza es distinta de otra si tienen alguna información distinta
	assert t1 != t3

import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from usuarioCliente import UsuarioCliente
from cita import Cita
from typing import List
import datetime

# Test comparación de cita médica
def test_compare_cita():
	# Creación usuario cliente
	u = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678")
	# Creación fecha
	fecha = datetime.datetime(2020, 5, 17)
	# Creación hora
	hora = datetime.time(3, 45, 12)
	
	# Creación de dos citas idénticas
	t1 = Cita("AU-77925767-1", u, "PR-77925767-1", fecha, hora, "D. Fernando", "Centro médico capital, Sala 2")
	t2 = Cita("AU-77925767-1", u, "PR-77925767-1", fecha, hora, "D. Fernando", "Centro médico capital, Sala 2")
	# Creación de una cita distinta
	t3 = Cita("AU-77925767-1", u, "PR-77925767-1", fecha, hora, "D. Miguel", "Centro médico capital, Sala 2")
	# Comprobar que una cita es igual a otra si tienen la misma información
	assert t1 == t2 # Pasa test
	# Comprobar que una cita es distinta de otra si tienen alguna información distinta
	assert t1 != t3

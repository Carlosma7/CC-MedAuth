import sys
import os
sys.path.append(os.path.abspath('./core/'))


from usuarioCliente import UsuarioCliente
from cita import Cita
from typing import List
import datetime

# Test comparación de cita médica
def test_compare_cita():
	u = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	fecha = datetime.datetime(2020, 5, 17)
	hora = datetime.time(3, 45, 12)
	
	t1 = Cita("AU-77925767-1", u, "PR-77925767-1", fecha, hora, "D. Fernando", "Centro médico capital, Sala 2")
	t2 = Cita("AU-77925767-1", u, "PR-77925767-1", fecha, hora, "D. Fernando", "Centro médico capital, Sala 2")
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test

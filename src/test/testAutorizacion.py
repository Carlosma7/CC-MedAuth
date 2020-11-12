import sys
import os
sys.path.append(os.path.abspath('./src/core/'))


from usuarioCliente import UsuarioCliente
from autorizacion import Autorizacion
from especialidad import Especialidad
from typing import List
import datetime




# Test comparación de autorizaciones	
def test_compare_autorizacion():
	u = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	fecha = datetime.datetime(2020, 5, 17)
	
	t1 = Autorizacion("AU-12345678", u, "MA-75925767-1", "PR-12345678", True, "", fecha, Especialidad.Traumatologia, ["Radiografía", "Ortopedia"], "D. Manuel", "Centro médico capital, Sala 2")
	t2 = Autorizacion("AU-12345678", u, "MA-75925767-1", "PR-12345678", True, "", fecha, Especialidad.Traumatologia, ["Radiografía", "Ortopedia"], "D. Manuel", "Centro médico capital, Sala 2")
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test

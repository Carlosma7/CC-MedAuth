import sys
import os
sys.path.append(os.path.abspath('./src/core/'))



from usuarioCliente import UsuarioCliente
from especialidad import Especialidad
from prescripcion import Prescripcion
from typing import List
import datetime



# Test comparación de prescripciones
def test_compare_prescripcion():
	u = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	fecha = datetime.datetime(2020, 5, 17)
	
	t1 = Prescripcion("PR-12345678", u, "MA-75925767-1", fecha, Especialidad.Traumatologia, "D. Fernando", "D. Juan", ["Radiografía", "Ortopedia"], "Centro médico capital, Sala 2")
	t2 = Prescripcion("PR-12345678", u, "MA-75925767-1", fecha, Especialidad.Traumatologia, "D. Fernando", "D. Juan", ["Radiografía", "Ortopedia"], "Centro médico capital, Sala 2")
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test

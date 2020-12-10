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
	# Creación usuario cliente
	u = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678")
	# Creación fecha
	fecha = datetime.datetime(2020, 5, 17)
	# Creación de dos prescripciones idénticas
	t1 = Prescripcion("PR-12345678", u, "MA-75925767-1", fecha, Especialidad.Traumatologia, "D. Fernando", "D. Juan", ["Radiografía", "Ortopedia"], "Centro médico capital, Sala 2")
	t2 = Prescripcion("PR-12345678", u, "MA-75925767-1", fecha, Especialidad.Traumatologia, "D. Fernando", "D. Juan", ["Radiografía", "Ortopedia"], "Centro médico capital, Sala 2")
	# Creación de una prescripción distinta
	t3 = Prescripcion("PR-12345678", u, "MA-75925767-1", fecha, Especialidad.Traumatologia, "D. Juan", "D. Juan", ["Radiografía", "Ortopedia"], "Centro médico capital, Sala 2")
	# Comprobar que una prescripción es igual a otra si tienen la misma información
	assert t1 == t2 # Pasa test
	# Comprobar que una prescripción es distinta de otra si tienen alguna información distinta
	assert t1 != t3

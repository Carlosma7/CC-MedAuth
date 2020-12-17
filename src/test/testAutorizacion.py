import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from usuarioCliente import UsuarioCliente
from autorizacion import Autorizacion
from especialidad import Especialidad
from typing import List
import datetime
from assertpy import assert_that

# Test comparación de autorizaciones	
def test_compare_autorizacion():
	# Creación usuario cliente
	u = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678")
	# Creación fecha
	fecha = datetime.datetime(2020, 5, 17)
	
	# Creación de dos autorizaciones idénticas
	t1 = Autorizacion("AU-12345678", u, "MA-75925767-1", "PR-12345678", True, "", fecha, Especialidad.Traumatologia, ["Radiografía", "Ortopedia"], "D. Manuel", "Centro médico capital, Sala 2")
	t2 = Autorizacion("AU-12345678", u, "MA-75925767-1", "PR-12345678", True, "", fecha, Especialidad.Traumatologia, ["Radiografía", "Ortopedia"], "D. Manuel", "Centro médico capital, Sala 2")
	# Creación de una autorización distinta
	t3 = Autorizacion("AU-12345678", u, "MA-75925767-1", "PR-12345678", True, "", fecha, Especialidad.Traumatologia, ["Radiografía", "Ortopedia"], "D. Carlos", "Centro médico capital, Sala 2")
	# Comprobar que una autorización es igual a otra si tienen la misma información
	assert_that(t1).is_equal_to(t2) # Pasa test
	# Comprobar que una autorización es distinta de otra si tienen alguna información distinta
	assert_that(t1).is_not_equal_to(t3) # Pasa test

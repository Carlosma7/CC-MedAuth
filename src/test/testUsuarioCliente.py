import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from usuarioCliente import UsuarioCliente
import pytest
from assertpy import assert_that

# Test comparación usuario cliente/asegurado
def test_compare_usuario_cliente():
	# Creación de dos usuarios clientes idénticos
	t1 = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678")
	t2 = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678")
	# Creación de un usuario cliente distinto
	t3 = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "22225767-F", "ES12345678")
	# Comprobar que un usuario cliente es igual a otro si tienen la misma información
	assert_that(t1).is_equal_to(t2) # Pasa test
	# Comprobar que un usuario cliente es distinto de otro si tienen alguna información distinta
	assert_that(t1).is_not_equal_to(t3) # Pasa test

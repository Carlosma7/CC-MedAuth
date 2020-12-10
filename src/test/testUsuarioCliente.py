import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from usuarioCliente import UsuarioCliente
import pytest

# Test comparación usuario cliente/asegurado
def test_compare_usuario_cliente():
	# Creación de dos usuarios clientes idénticos
	t1 = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678")
	t2 = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678")
	# Creación de un usuario cliente distinto
	t3 = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "22225767-F", "ES12345678")
	# Comprobar que un usuario cliente es igual a otro si tienen la misma información
	assert t1 == t2 # Pasa test
	# Comprobar que un usuario cliente es distinto de otro si tienen alguna información distinta
	assert t1 != t3

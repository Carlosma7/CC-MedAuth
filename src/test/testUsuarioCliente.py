import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from usuarioCliente import UsuarioCliente

import pytest


# Test comparación usuario cliente/asegurado
def test_compare_usuario_cliente():
	t1 = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678")
	t2 = UsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678")
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test

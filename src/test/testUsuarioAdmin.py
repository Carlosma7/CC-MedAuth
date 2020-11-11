import sys
import os
sys.path.append(os.path.abspath('./core/'))

from usuarioAdmin import UsuarioAdmin

import pytest


# Test comparación usuario administrativo
def test_compare_usuario_admin():
	t1 = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "carlos@medauth.com")
	t2 = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "carlos@medauth.com")
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test

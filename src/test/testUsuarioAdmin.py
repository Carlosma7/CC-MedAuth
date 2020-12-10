import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from usuarioAdmin import UsuarioAdmin
import pytest

# Test comparación usuario administrativo
def test_compare_usuario_admin():
	# Creación de dos usuarios administrativos idénticos
	t1 = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "carlos@medauth.com")
	t2 = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "carlos@medauth.com")
	# Creación de un usuario administrativo distinto
	t3 = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "morales@medauth.com")
	# Comprobar que un usuario admin es igual a otro si tienen la misma información
	assert t1 == t2 # Pasa test
	# Comprobar que un usuario admin es distinto de otro si tienen alguna información distinta
	assert t1 != t3

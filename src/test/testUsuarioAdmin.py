import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from usuarioAdmin import UsuarioAdmin
import pytest
from assertpy import assert_that

# Test comparación usuario administrativo
def test_compare_usuario_admin():
	# Creación de dos usuarios administrativos idénticos
	t1 = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "carlos@medauth.com")
	t2 = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "carlos@medauth.com")
	# Creación de un usuario administrativo distinto
	t3 = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "morales@medauth.com")
	# Comprobar que un usuario admin es igual a otro si tienen la misma información
	assert_that(t1).is_equal_to(t2) # Pasa test
	# Comprobar que un usuario admin es distinto de otro si tienen alguna información distinta
	assert_that(t1).is_not_equal_to(t3) # Pasa test

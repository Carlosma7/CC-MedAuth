import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from usuario import Usuario
import pytest
from assertpy import assert_that

# Test comparación usuario genérico
def test_compare_usuario():
	# Creación de dos usuarios idénticos
	t1 = Usuario("Carlos", "carlos7ma@gmail.com", "75212389-Z", 0)
	t2 = Usuario("Carlos", "carlos7ma@gmail.com", "75212389-Z", 0)
	# Creación de un usuario distinto
	t3 = Usuario("Carlos", "carlos7ma@gmail.com", "75212389-Z", 1)
	# Comprobar que un usuario es igual a otro si tienen la misma información
	assert_that(t1).is_equal_to(t2) # Pasa test
	# Comprobar que un usuario es distinto de otro si tienen alguna información distinta
	assert_that(t1).is_not_equal_to(t3) # Pasa test

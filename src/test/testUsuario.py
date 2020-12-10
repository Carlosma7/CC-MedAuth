import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from usuario import Usuario
import pytest

# Test comparación usuario genérico
def test_compare_usuario():
	# Creación de dos usuarios idénticos
	t1 = Usuario("Carlos", "carlos7ma@gmail.com", "75212389-Z", 0)
	t2 = Usuario("Carlos", "carlos7ma@gmail.com", "75212389-Z", 0)
	# Creación de un usuario distinto
	t3 = Usuario("Carlos", "carlos7ma@gmail.com", "75212389-Z", 1)
	# Comprobar que una prescripción es igual a otra si tienen la misma información
	assert t1 == t2 # Pasa test
	# Comprobar que una prescripción es distinta de otra si tienen alguna información distinta
	assert t1 != t3

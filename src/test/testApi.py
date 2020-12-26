import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from main import *
import pytest
import json
from assertpy import assert_that

@pytest.fixture(name='test_medauth')
def _test_medauth():
	return app

# Test creacion usuario
@pytest.mark.asyncio
async def test_crear_admin_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/usuario/crear'
	
	# Crear usuario administrativo
	usuario = UsuarioAdmin('Carlos', 'carlos7ma@gmail.com', '75925767-F', '')
	tipo = 0
	
	# Lanzar petición
	response = await client.post(url, data = json.dumps({'usuario': usuario.to_dict(), 'tipo': tipo}))
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

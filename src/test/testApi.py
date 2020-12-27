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

# Test creacion usuario administrativo
@pytest.mark.asyncio
async def test_crear_admin_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/usuario/crear'
	
	# Crear usuario administrativo
	usuario = UsuarioAdmin('Alfredo', 'alfredo@gmail.com', '35925767-A', '')
	tipo = 0
	
	# Lanzar petición
	response = await client.post(url, data = json.dumps({'usuario': usuario.to_dict(), 'tipo': tipo}))
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

# Test creacion usuario cliente
@pytest.mark.asyncio
async def test_crear_cliente_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/usuario/crear'
	
	# Crear usuario administrativo
	usuario = UsuarioCliente('Roberto', 'rober@gmail.com', '25123540-F', 'ES1234111892738495273840')
	tipo = 1
	
	# Lanzar petición
	response = await client.post(url, data = json.dumps({'usuario': usuario.to_dict(), 'tipo': tipo}))
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

# Test de modificación de administrador
@pytest.mark.asyncio
async def test_modificar_admin_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/usuario/modificar'
	
	# Crear usuario administrativo
	usuario = UsuarioAdmin('Alfredo', 'alfredo@gmail.com', '35925767-A', '')
	tipo = 0
	nombre = 'Alfredo'
	email = 'alfred1@gmail.com'
	cuenta_bancaria = ''
	
	# Lanzar petición
	response = await client.post(url, data = json.dumps({'usuario': usuario.to_dict(), 'tipo': tipo, 'nombre': nombre, 'email': email, 'cuenta_bancaria': cuenta_bancaria}))
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

# Test de modificación de cliente
@pytest.mark.asyncio
async def test_modificar_cliente_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/usuario/modificar'
	
	# Crear usuario cliente
	usuario = UsuarioCliente('Roberto', 'rober@gmail.com', '25123540-F', 'ES1234111892738495273840')
	tipo = 1
	nombre = 'Roberto'
	email = 'rober@gmail.com'
	cuenta_bancaria = 'ES1234111892738495270000'
	
	# Lanzar petición
	response = await client.post(url, data = json.dumps({'usuario': usuario.to_dict(), 'tipo': tipo, 'nombre': nombre, 'email': email, 'cuenta_bancaria': cuenta_bancaria}))
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)
	
# Test de eliminar administrador
@pytest.mark.asyncio
async def test_eliminar_admin_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/usuario/35925767-A'
	
	# Lanzar petición
	response = await client.delete(url)
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

# Test de eliminar cliente
@pytest.mark.asyncio
async def test_eliminar_cliente_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/usuario/25123540-F'
	
	# Lanzar petición
	response = await client.delete(url)
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

# Test de crear póliza
@pytest.mark.asyncio
async def test_crear_poliza_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/usuario/crear'
	
	# Crear usuario administrativo
	usuario = UsuarioCliente('Roberto', 'rober@gmail.com', '25123540-F', 'ES1234111892738495273840')
	tipo = 1
	
	# Lanzar petición
	response = await client.post(url, data = json.dumps({'usuario': usuario.to_dict(), 'tipo': tipo}))
	
	# Crear url
	url = '/poliza/crear'

	# Creación fecha
	fecha = datetime.datetime(2020, 5, 17)
	# Creación objeto Póliza
	poliza = Poliza(usuario, usuario.get_dni(), fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	
	# Lanzar petición
	response = await client.post(url, data = json.dumps(poliza.to_dict()))
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

# Test de modificar póliza
@pytest.mark.asyncio
async def test_modificar_poliza_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/poliza/modificar'

	# Crear usuario cliente
	usuario = UsuarioCliente('Roberto', 'rober@gmail.com', '25123540-F', 'ES1234111892738495273840')
	# Creación fecha
	fecha = datetime.datetime(2020, 5, 17)
	# Creación objeto Póliza
	poliza = Poliza(usuario, "MA-25123540-1", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	# Creación periodo carencia
	periodo_carencia = fecha.strftime('%m/%d/%Y')
	# Creación tipo póliza
	tipo = TipoPoliza.Basica
	# Creación copagos y mensualidad, cambiando los copagos como modificación
	copagos = 10.99
	mensualidad = 50.99
	# Creación servicios_excluidos
	servicios_excluidos = ["TAC", "Apendicitis"]
	# Creación módulos extra
	modulos_extra = [ModuloExtra.Dental]
	
	# Lanzar petición
	response = await client.post(url, data = json.dumps({'poliza': poliza.to_dict(), 'periodo_carencia': periodo_carencia, 'tipo': tipo, 'copagos': copagos, 'mensualidad': mensualidad, 'servicios_excluidos': servicios_excluidos, 'modulos_extra': modulos_extra}))
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

# Test de consultar póliza
@pytest.mark.asyncio
async def test_consultar_poliza_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/poliza/25123540-F'

	# Lanzar petición
	response = await client.get(url)
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

# Test de desactivar póliza
@pytest.mark.asyncio
async def test_desactivar_poliza_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/poliza/25123540-F'

	# Lanzar petición
	response = await client.post(url)
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

# Test de subir prescripción
@pytest.mark.asyncio
async def test_subir_prescripcion_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	
	# Crear url
	url = '/poliza/crear'
	
	# Crear usuario cliente
	usuario = UsuarioCliente('Roberto', 'rober@gmail.com', '25123540-F', 'ES1234111892738495273840')
	# Creación fecha
	fecha = datetime.datetime(2020, 5, 17)
	# Creación objeto Póliza
	poliza = Poliza(usuario, usuario.get_dni(), fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	# Lanzar petición
	response = await client.post(url, data = json.dumps(poliza.to_dict()))
	
	# Crear url
	url = '/prescripcion'
	
	# Creación fecha
	fecha_realizacion = datetime.datetime(2020, 6, 22)
	# Creación prescripción con usuario y póliza
	prescripcion = Prescripcion(usuario.get_dni(), usuario, 'MA-25123540-2', fecha_realizacion, Especialidad.Epidemiologia, "D. Miguel", "D. Fernando", ["Serología", "PCR"], "Consulta 3")

	# Lanzar petición
	response = await client.post(url, data = json.dumps(prescripcion.to_dict()))
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

# Test de solicitar autorización
@pytest.mark.asyncio
async def test_solicitar_autorizacion_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/autorizacion/PR-25123540-1'

	# Lanzar petición
	response = await client.post(url)
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

# Test de crear autorización
@pytest.mark.asyncio
async def test_crear_autorizacion_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	
	# Crear usuario administrativo
	usuario = UsuarioCliente('Roberto', 'rober@gmail.com', '25123540-F', 'ES1234111892738495273840')
	# Crear url
	url = '/autorizacion/crear'

	# Creación fecha
	fecha_realizacion = datetime.datetime(2020, 6, 22)
	# Creación autorización con usuario y póliza
	autorizacion = Autorizacion('', usuario, '', 'MA-25123540-2', True, '', fecha_realizacion, Especialidad.Epidemiologia, ["Serología", "PCR"], "D. Miguel", "Consulta 3")
	
	# Lanzar petición
	response = await client.post(url, data = json.dumps(autorizacion.to_dict()))
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

# Test de modificar autorizacion
@pytest.mark.asyncio
async def test_modificar_autorizacion_api(test_medauth):
	# Obtener el servidor de la app
	client = app.test_client()
	# Crear url
	url = '/autorizacion/modificar'

	# Crear usuario cliente
	usuario = UsuarioCliente('Roberto', 'rober@gmail.com', '25123540-F', 'ES1234111892738495273840')
	# Creación fecha
	fecha_realizacion = datetime.datetime(2020, 6, 22)
	# Creación autorización con usuario y póliza
	autorizacion = Autorizacion('AU-25123540-2', usuario, '', 'MA-25123540-2', True, '', fecha_realizacion, Especialidad.Epidemiologia, ["Serología", "PCR"], "D. Miguel", "Consulta 3")
	
	# Creación motivo rechazo
	motivo_rechazo = ''
	# Creación fecha realizacion
	fecha_realizacion = fecha_realizacion.strftime('%m/%d/%Y')
	# Creación especialidad
	especialidad = Especialidad.Epidemiologia
	# Creación servicios aceptados
	servicios_aceptados = ["Serología", "PCR"]
	# Creación facultativo realizador
	facultativo_realizador = "D. Carlos"
	# Creación consulta
	consulta = "Consulta 3"
	
	# Lanzar petición
	response = await client.post(url, data = json.dumps({'autorizacion': autorizacion.to_dict(), 'motivo_rechazo': motivo_rechazo, 'fecha_realizacion': fecha_realizacion, 'especialidad': json.dumps(especialidad), 'servicios_aceptados': servicios_aceptados, 'facultativo_realizador': facultativo_realizador, 'consulta': consulta}))
	# Comprobar que el estado es correcto
	assert_that(response.status_code).is_equal_to(200)

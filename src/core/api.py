from controlador import *

from quart import Quart, Blueprint, jsonify, request
import json

# Controlador de la lógica de negocio
controlador = Controller()

# Definición de Blueprint
rutas_medauth = Blueprint("rutas_medauth", __name__)

# [HU1] Creación usuario administrativo
# [HU2] Creación usuario asegurado
@rutas_medauth.route('/usuario/crear', methods=['POST'])
async def crear_usuario():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener usuario
	usuario = data.get('usuario')
	# Obtener tipo 
	tipo = data.get('tipo')
	
	# Crear usuario con la información
	if tipo == 0: # Usuario administrativo
		usuario = UsuarioAdmin(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('email_empresarial'))
	else: # Usuario cliente
		usuario = UsuarioCliente(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('cuenta_bancaria'))
	
	try:
		# Creación usuario
		controlador.crear_usuario(usuario, tipo)
	except ValueError as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Usuario creado con éxito.', 200

# [HU3] Administrar usuario: Modificar usuario
@rutas_medauth.route('/usuario/modificar', methods=['POST'])
async def modificar_usuario():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener usuario
	usuario = data.get('usuario')
	# Obtener nombre 
	nombre = data.get('nombre')
	# Obtener email
	email = data.get('email')
	# Obtener cuenta bancaria
	cuenta_bancaria = data.get('cuenta_bancaria')
	# Obtener tipo
	tipo = data.get('tipo')
	
	
	# Crear usuario con la información
	if tipo == 0: # Usuario administrativo
		usuario = UsuarioAdmin(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), '')
	else: # Usuario cliente
		usuario = UsuarioCliente(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), '')
	
	try:
		# Modificación usuario
		controlador.modificar_usuario(usuario, nombre, email, cuenta_bancaria)
	except ValueError as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Usuario modificado con éxito.', 200

# [HU3] Administrar usuario: Eliminar usuario
@rutas_medauth.route('/usuario/<dni>', methods=['DELETE'])
async def eliminar_usuario(dni):
	try:
		# Eliminación usuario
		controlador.eliminar_usuario(dni)
	except ValueError as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Usuario eliminado con éxito.', 200

# [HU4] Administrar póliza: Crear una póliza
@rutas_medauth.route('/poliza/crear', methods=['POST'])
async def crear_poliza():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener titular
	titular = data.get('titular')
	titular = UsuarioCliente(titular.get('nombre'), titular.get('email'), titular.get('dni'), titular.get('cuenta_bancaria'))
	# Obtener periodo carencia
	periodo_carencia = datetime.datetime.strptime(data.get('periodo_carencia'), '%m/%d/%Y')
	# Obtener tipo de póliza
	tipo = TipoPoliza(json.loads(data.get('tipo')))
	# Obtener modulos extra
	modulos_extra = [ModuloExtra(mod) for mod in data.get('modulos_extra')]
	# Crear Póliza
	poliza = Poliza(titular, data.get('id_poliza'), periodo_carencia, tipo, data.get('copagos'), data.get('mensualidad'), data.get('servicios_excluidos'), modulos_extra, data.get('activa'))
	
	try:
		# Creación póliza
		controlador.crear_poliza(poliza)
	except ValueError as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Póliza creada con éxito.', 200

# [HU4] Administrar póliza: Modificar una póliza
@rutas_medauth.route('/poliza/modificar', methods=['POST'])
async def modificar_poliza():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener póliza
	poliza = data.get('poliza')
	# Obtener titular de la póliza
	titular = poliza.get('titular')
	titular = UsuarioCliente(titular.get('nombre'), titular.get('email'), titular.get('dni'), titular.get('cuenta_bancaria'))
	# Obtener periodo carencia de la póliza
	periodo_carencia = datetime.datetime.strptime(poliza.get('periodo_carencia'), '%m/%d/%Y')
	# Obtener tipo de póliza de la póliza
	tipo = TipoPoliza(json.loads(poliza.get('tipo')))
	# Obtener modulos extra de la póliza
	modulos_extra = [ModuloExtra(mod) for mod in poliza.get('modulos_extra')]
	# Crear Póliza
	poliza = Poliza(titular, poliza.get('id_poliza'), periodo_carencia, tipo, poliza.get('copagos'), poliza.get('mensualidad'), poliza.get('servicios_excluidos'), modulos_extra, poliza.get('activa'))
	
	# Obtener periodo carencia
	periodo_carencia = datetime.datetime.strptime(data.get('periodo_carencia'), '%m/%d/%Y')
	# Obtener tipo de póliza
	tipo = data.get('tipo')
	# Obtener copagos
	copagos = data.get('copagos')
	# Obtener mensualidad
	mensualidad = data.get('mensualidad')
	# Obtener servicios excluidos
	servicios_excluidos = data.get('servicios_excluidos')
	# Obtener modulos extra
	modulos_extra = [ModuloExtra(mod) for mod in data.get('modulos_extra')]
	try:
		# Modificación póliza
		controlador.modificar_poliza(poliza, periodo_carencia, tipo, copagos, mensualidad, servicios_excluidos, modulos_extra)
	except ValueError as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Póliza modificada con éxito.', 200

# [HU4] Administrar póliza: Desactivar una póliza
@rutas_medauth.route('/poliza/<dni>', methods=['POST'])
async def desactivar_poliza(dni):
	try:
		# Desactivación póliza
		controlador.desactivar_poliza(dni)
	except ValueError as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Póliza desactivada con éxito.', 200

# [HU5] Consultar póliza
@rutas_medauth.route('/poliza/<dni>', methods=['GET'])
async def consultar_poliza(dni):
	try:
		# Desactivación póliza
		poliza = controlador.consultar_poliza(dni)
	except ValueError as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return poliza.to_dict(), 200

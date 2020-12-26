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
	return 'Usuario creado', 200

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
		# Creación usuario
		controlador.modificar_usuario(usuario, nombre, email, cuenta_bancaria)
	except ValueError as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Usuario creado', 200

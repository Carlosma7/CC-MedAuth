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
	else:
		usuario = UsuarioCliente(usuario.get('nombre'), usuario.get('email'), usuario.get('dni'), usuario.get('cuenta_bancaria'))
	
	try:
		# Creación usuario
		controlador.crear_usuario(usuario, tipo)
	except ValueError as error:
		# Se produce un error
		return str(error), 400
	
	# Estado de éxito
	return 'Usuario creado', 200

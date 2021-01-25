from controlador import *

from quart import Quart, Blueprint, jsonify, request
import json
from loguru import logger

# Controlador de la lógica de negocio
controlador = Controller()

# Definición de Blueprint
rutas_medauth = Blueprint("rutas_medauth", __name__)

# [HU1] Creación usuario administrativo
# [HU2] Creación usuario asegurado
@rutas_medauth.route('/usuarios', methods=['POST'])
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
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Usuario creado con éxito')
	# Estado de éxito
	return 'Usuario creado con éxito.', 201

# [HU3] Administrar usuario: Modificar usuario
@rutas_medauth.route('/usuarios/modificar/<dni>', methods=['POST'])
async def modificar_usuario(dni):
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener nombre 
	nombre = data.get('nombre')
	# Obtener email
	email = data.get('email')
	# Obtener cuenta bancaria
	cuenta_bancaria = data.get('cuenta_bancaria')
	# Obtener tipo
	tipo = data.get('tipo')
	
	try:
		# Modificación usuario
		controlador.modificar_usuario(dni, nombre, email, cuenta_bancaria)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Usuario modificado con éxito')
	# Estado de éxito
	return 'Usuario modificado con éxito.', 201

# [HU3] Administrar usuario: Eliminar usuario
@rutas_medauth.route('/usuarios/<dni>', methods=['DELETE'])
async def eliminar_usuario(dni):
	try:
		# Eliminación usuario
		controlador.eliminar_usuario(dni)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Usuario eliminado con éxito')
	# Estado de éxito
	return 'Usuario eliminado con éxito.', 200

# [HU4] Administrar póliza: Crear una póliza
@rutas_medauth.route('/polizas', methods=['POST'])
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
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Póliza creada con éxito')
	# Estado de éxito
	return 'Póliza creada con éxito.', 201

# [HU4] Administrar póliza: Modificar una póliza
@rutas_medauth.route('/polizas/modificar/<id_poliza>', methods=['POST'])
async def modificar_poliza(id_poliza):
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
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
		controlador.modificar_poliza(id_poliza, periodo_carencia, tipo, copagos, mensualidad, servicios_excluidos, modulos_extra)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Póliza modificada con éxito')
	# Estado de éxito
	return 'Póliza modificada con éxito.', 201

# [HU4] Administrar póliza: Desactivar una póliza
@rutas_medauth.route('/polizas/desactivar/<dni>', methods=['POST'])
async def desactivar_poliza(dni):
	try:
		# Desactivación póliza
		controlador.desactivar_poliza(dni)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Póliza desactivada con éxito')
	# Estado de éxito
	return 'Póliza desactivada con éxito.', 201

# [HU5] Consultar póliza
@rutas_medauth.route('/polizas/<dni>', methods=['GET'])
async def consultar_poliza(dni):
	try:
		# Consultar póliza
		poliza = controlador.consultar_poliza(dni)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Póliza obtenida con éxito')
	# Estado de éxito
	return poliza.to_dict(), 200

# [HU6] Subir prescripción médica
@rutas_medauth.route('/prescripciones', methods=['POST'])
async def subir_prescripcion():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener asegurado
	asegurado = data.get('asegurado')
	asegurado = UsuarioCliente(asegurado.get('nombre'), asegurado.get('email'), asegurado.get('dni'), asegurado.get('cuenta_bancaria'))
	# Obtener fecha realización
	fecha_realizacion = datetime.datetime.strptime(data.get('fecha_realizacion'), '%m/%d/%Y')
	# Obtener especialidad
	especialidad = Especialidad(json.loads(data.get('especialidad')))
	# Subir Prescripción
	prescripcion = Prescripcion('', asegurado, data.get('id_poliza'), fecha_realizacion, especialidad, data.get('facultativo_prescriptor'), data.get('facultativo_realizador'), data.get('servicios_solicitados'), data.get('consulta'))
	
	try:
		# Subir prescripcion
		controlador.subir_prescripcion(prescripcion)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Prescripción subida con éxito')
	# Estado de éxito
	return 'Prescripción subida con éxito.', 201

# [HU7] Solicitar autorización médica
@rutas_medauth.route('/autorizaciones/solicitar/<id_prescripcion>', methods=['POST'])
async def solicitar_autorizacion(id_prescripcion):
	try:
		# Solicitar autorizacion
		controlador.solicitar_autorizacion(id_prescripcion)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Autorización solicitada con éxito')
	# Estado de éxito
	return 'Autorización solicitada con éxito.', 201

# [HU8] Administrar autorización: Crear una autorización
@rutas_medauth.route('/autorizaciones', methods=['POST'])
async def crear_autorizacion():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener asegurado
	asegurado = data.get('asegurado')
	asegurado = UsuarioCliente(asegurado.get('nombre'), asegurado.get('email'), asegurado.get('dni'), asegurado.get('cuenta_bancaria'))
	# Obtener fecha realización
	fecha_realizacion = datetime.datetime.strptime(data.get('fecha_realizacion'), '%m/%d/%Y')
	# Obtener especialidad
	especialidad = Especialidad(json.loads(data.get('especialidad')))
	# Crear Autorizacion
	autorizacion = Autorizacion('', asegurado, '', data.get('id_poliza'), data.get('aceptada'), data.get('motivo_rechazo'), fecha_realizacion, especialidad, data.get('servicios_aceptados'), data.get('facultativo_realizador'), data.get('consulta'))
	
	try:
		# Crear autorización
		controlador.crear_autorizacion(autorizacion)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Autorización creada con éxito')
	# Estado de éxito
	return 'Autorización creada con éxito.', 201

# [HU8] Administrar autorización: Modificar una autorización
@rutas_medauth.route('/autorizaciones/modificar/<id_autorizacion>', methods=['POST'])
async def modificar_autorizacion(id_autorizacion):
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener motivo rechazo
	motivo_rechazo = data.get('motivo_rechazo')
	# Obtener fecha realizacion
	fecha_realizacion = datetime.datetime.strptime(data.get('fecha_realizacion'), '%m/%d/%Y')
	# Obtener especialidad
	especialidad = Especialidad(json.loads(data.get('especialidad')))
	# Obtener servicios aceptados
	servicios_aceptados = data.get('servicios_aceptados')
	# Obtener facultativo realizador
	facultativo_realizador = data.get('facultativo_realizador')
	# Obtener consulta
	consulta = data.get('consulta')
	
	try:
		# Modificación autorización
		controlador.modificar_autorizacion(id_autorizacion, motivo_rechazo, fecha_realizacion, especialidad, servicios_aceptados, facultativo_realizador, consulta)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Autorización modificada con éxito')
	# Estado de éxito
	return 'Autorización modificada con éxito.', 201

# [HU9] Consultar autorización médica
@rutas_medauth.route('/autorizaciones/<id_autorizacion>', methods=['GET'])
async def consultar_autorizacion(id_autorizacion):
	try:
		# Consultar autorizacion
		autorizacion = controlador.consultar_autorizacion(id_autorizacion)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Autorización obtenida con éxito')
	# Estado de éxito
	return autorizacion.to_dict(), 200

# [HU10] Aprobar/Denegar una autorización médica
@rutas_medauth.route('/autorizaciones/aprobar-denegar/<id_autorizacion>', methods=['POST'])
async def aprobar_denegar_autorizacion(id_autorizacion):
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
		
	# Obtener aceptada
	aceptada = data.get('aceptada')
	# Obtener motivo rechazo
	motivo_rechazo = data.get('motivo_rechazo')
	
	try:
		# Aprobar/Denegar autorización
		controlador.aprobar_denegar_autorizacion(id_autorizacion, aceptada, motivo_rechazo)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Autorización aprobada/denegada con éxito')
	# Estado de éxito
	return 'Autorización aprobada/denegada con éxito.', 201

# [HU11] Administrar cita médica: Crear cita médica
@rutas_medauth.route('/citas', methods=['POST'])
async def crear_cita():
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener asegurado
	asegurado = data.get('asegurado')
	asegurado = UsuarioCliente(asegurado.get('nombre'), asegurado.get('email'), asegurado.get('dni'), asegurado.get('cuenta_bancaria'))
	# Obtener fecha
	fecha = datetime.datetime.strptime(data.get('fecha'), '%m/%d/%Y')
	# Obtener hora
	hora = datetime.datetime.strptime(data.get('hora'), '%H:%M')
	# Crear Cita
	cita = Cita(data.get('id_autorizacion'), asegurado, data.get('id_prescripcion'), fecha, hora, data.get('facultativo_realizador'), data.get('consulta'))
	
	try:
		# Crear cita
		controlador.crear_cita(cita)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Cita creada con éxito')
	# Estado de éxito
	return 'Cita creada con éxito.', 201

# [HU11] Administrar cita médica: Modificar cita médica
@rutas_medauth.route('/citas/modificar/<id_cita>', methods=['POST'])
async def modificar_cita(id_cita):
	# Obtener la petición
	data_string = await request.get_data()
	# Cargar información de la petición en formato JSON
	data = json.loads(data_string)
	
	# Obtener fecha
	fecha = datetime.datetime.strptime(data.get('fecha'), '%m/%d/%Y')
	# Obtener hora
	hora = datetime.datetime.strptime(data.get('hora'), '%H:%M')
	# Obtener facultativo realizador
	facultativo_realizador = data.get('facultativo_realizador')
	# Obtener consulta
	consulta = data.get('consulta')
	
	try:
		# Modificación cita
		controlador.modificar_cita(id_cita, fecha, hora, facultativo_realizador, consulta)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Cita modificada con éxito')
	# Estado de éxito
	return 'Cita modificada con éxito.', 201

# [HU12] Consultar cita médica
@rutas_medauth.route('/citas/<id_autorizacion>', methods=['GET'])
async def consultar_cita(id_autorizacion):
	try:
		# Consultar cita
		autorizacion = controlador.consultar_cita(id_autorizacion)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Cita obtenida con éxito')
	# Estado de éxito
	return autorizacion.to_dict(), 200

# [HU14] Consultar usuario
@rutas_medauth.route('/usuarios/<dni>', methods=['GET'])
async def consultar_usuario(dni):
	try:
		# Consultar usuario
		usuario = controlador.consultar_usuario(dni)
	except Exception as error:
		# Se transmite el error mediante el log
		logger.error(error)
		# Se produce un error
		return str(error), 400
	
	# Se transmite el estado de éxito mediante el log	
	logger.info('Usuario obtenido con éxito')
	# Estado de éxito
	return usuario.to_dict(), 200

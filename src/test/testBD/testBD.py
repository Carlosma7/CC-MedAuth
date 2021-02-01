import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from controlador import *

import pytest
from assertpy import assert_that

# Test de creación de usuario administrativo
def test_crear_admin():
	controlador = Controller()
	# Creación de usuario administrador
	admin = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "")
	
	# Comprobar que no existe el usuario en BD
	assert_that(controlador.mongo.db.usuarios.find({'dni':admin.get_dni()}).count()).is_equal_to(0)
	# Crear administrador
	controlador.crear_usuario(admin, 0)
	# Comprobar que existe el usuario en BD
	assert_that(controlador.mongo.db.usuarios.find({'dni':admin.get_dni()}).count()).is_equal_to(1)
	
# Test de creación de usuario cliente/asegurado
def test_crear_cliente():
	controlador = Controller()
	# Creación de usuario cliente
	cliente = UsuarioCliente("Juan", "juan@gmail.com", "75123540-F", "ES1234111892738495273849")
	
	# Comprobar que no existe el usuario en BD
	assert_that(controlador.mongo.db.usuarios.find({'dni':cliente.get_dni()}).count()).is_equal_to(0)
	# Crear cliente
	controlador.crear_usuario(cliente, 1)
	# Comprobar que existe el usuario en BD
	assert_that(controlador.mongo.db.usuarios.find({'dni':cliente.get_dni()}).count()).is_equal_to(1)
	
# Test de modificación de administrador
def test_modificar_admin():
	controlador = Controller()
	# Creación de usuario administrador
	adminAntiguo = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "")
	# Modificación de usuario administrador
	controlador.modificar_usuario(adminAntiguo.get_dni(), 'Carlos', 'charles@gmail.com', "")
	# Obtengo el usuario administrador almacenado
	adminNuevo = controlador.mongo.db.usuarios.find_one({'dni': adminAntiguo.get_dni()})
	adminNuevo = UsuarioAdmin.from_dict(adminNuevo)
	# Comprobar que el administrador es diferente tras la modificación
	assert_that(adminAntiguo).is_not_equal_to(adminNuevo)
	# Comprobar que es el mismo DNI
	assert_that(adminNuevo.get_dni()).is_equal_to(adminAntiguo.get_dni())

# Test de modificación de cliente
def test_modificar_cliente():
	controlador = Controller()
	# Creación de usuario cliente
	clienteAntiguo = UsuarioCliente("Juan", "juan@gmail.com", "75123540-F", "ES1234111892738495273849")
	# Modificación de usuario cliente
	controlador.modificar_usuario(clienteAntiguo.get_dni(), 'Juan', 'juan@gmail.com', "ES1298742874928365740192")
	# Obtengo el usuario cliente almacenado
	clienteNuevo = controlador.mongo.db.usuarios.find_one({'dni': clienteAntiguo.get_dni()})
	clienteNuevo = UsuarioCliente.from_dict(clienteNuevo)
	# Comprobar que el cliente es diferente tras la modificación
	assert_that(clienteAntiguo).is_not_equal_to(clienteNuevo)
	# Comprobar que es el mismo DNI
	assert_that(clienteNuevo.get_dni()).is_equal_to(clienteAntiguo.get_dni())

# Test de eliminar administración
def test_eliminar_admin():
	controlador = Controller()
	# Creación de usuario administrativo
	admin = UsuarioAdmin("Carlos", "charles@gmail.com", "75925767-F", "charles@medauth.com")
	# Comprobar que existe el usuario en BD
	assert_that(controlador.mongo.db.usuarios.find({'dni':admin.get_dni()}).count()).is_equal_to(1)
	# Eliminar el usuario administrativo
	controlador.eliminar_usuario(admin.get_dni())
	# Comprobar que ya no existe el usuario en BD
	assert_that(controlador.mongo.db.usuarios.find({'dni':admin.get_dni()}).count()).is_equal_to(0)

# Test de eliminar cliente
def test_eliminar_cliente():
	controlador = Controller()
	# Creación de usuario cliente
	cliente = UsuarioCliente("Juan", "juan@gmail.com", "75123540-F", "ES1298742874928365740192")
	# Comprobar que existe el usuario en BD
	assert_that(controlador.mongo.db.usuarios.find({'dni':cliente.get_dni()}).count()).is_equal_to(1)
	# Eliminar el usuario cliente
	controlador.eliminar_usuario(cliente.get_dni())
	# Comprobar que ya no existe el usuario en BD
	assert_that(controlador.mongo.db.usuarios.find({'dni':cliente.get_dni()}).count()).is_equal_to(0)

# Test de creación de póliza
def test_crear_poliza():
	controlador = Controller()
	# Creación de usuario cliente
	cliente = UsuarioCliente("Alejandro", "alex@gmail.com", "75125767-F", "ES9934567899283722194827")
	# Crear cliente
	controlador.crear_usuario(cliente, 1)

	# Creación fecha
	fecha = datetime.datetime(2020, 5, 17)
	# Creación objeto Póliza
	p = Poliza(cliente, cliente.get_dni(), fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	# Comprobar que no existe la póliza en el controlador
	assert_that(controlador.mongo.db.polizas.find({'id_poliza': p.get_id_poliza()}).count()).is_equal_to(0)
	# Crear póliza
	controlador.crear_poliza(p)
	# Comprobar que la póliza ya si existe en el controlador
	assert_that(controlador.mongo.db.polizas.find({'id_poliza': p.get_id_poliza()}).count()).is_equal_to(1)

# Test de modificación de póliza
def test_modificar_poliza():
	controlador = Controller()
	# Obtener cliente por el DNI
	cliente = controlador.mongo.db.usuarios.find_one({'dni': '75125767-F'})
	
	if cliente != None:
		cliente = UsuarioCliente.from_dict(cliente)
		# Creación fecha
		fecha = datetime.datetime(2020, 5, 17)
		# Creación objeto Póliza
		polizaAntigua = Poliza(cliente, "MA-75125767-1", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		# Modificación de póliza
		controlador.modificar_poliza(polizaAntigua.get_id_poliza(), fecha, TipoPoliza.Basica, 10.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental])
		# Obtengo la poliza almacenada
		polizaNueva = controlador.mongo.db.polizas.find_one({'id_poliza': polizaAntigua.get_id_poliza()})
		polizaNueva = Poliza.from_dict(polizaNueva)
		# Comprobar que el cliente es diferente tras la modificación
		assert_that(polizaAntigua).is_not_equal_to(polizaNueva)
		# Comprobar que es el mismo DNI
		assert_that(polizaAntigua.get_id_poliza()).is_equal_to(polizaNueva.get_id_poliza())


# Test de consulta de póliza
def test_consultar_poliza():
	controlador = Controller()
	# Obtener cliente por el DNI
	cliente = controlador.mongo.db.usuarios.find_one({'dni': '75125767-F'})
	
	if cliente != None:
		cliente = UsuarioCliente.from_dict(cliente)
		# Creación fecha
		fecha = datetime.datetime(2020, 5, 17)
		# Creación objeto Póliza
		poliza1 = Poliza(cliente, "MA-75125767-1", fecha, TipoPoliza.Basica, 10.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		# Consultar póliza del controlador con el DNI del asegurado asociado
		poliza2 = controlador.consultar_poliza("75125767-F")
		# Comprobar que la póliza obtenida es igual, y por lo tanto la consulta es correcta
		assert_that(poliza1).is_equal_to(poliza2)

# Test de desactivar póliza
def test_desactivar_poliza():
	controlador = Controller()
	# Obtener cliente por el DNI
	cliente = controlador.mongo.db.usuarios.find_one({'dni': '75125767-F'})
	
	if cliente != None:
		cliente = UsuarioCliente.from_dict(cliente)
		# Creación fecha
		fecha = datetime.datetime(2020, 5, 17)
		# Creación objeto Póliza activa
		polizaAntigua = Poliza(cliente, "MA-75125767-1", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		# Desactivación de la póliza
		controlador.desactivar_poliza(polizaAntigua.get_titular().get_dni())
		# Obtengo la poliza almacenada
		polizaNueva = controlador.mongo.db.polizas.find_one({'id_poliza': polizaAntigua.get_id_poliza()})
		polizaNueva = Poliza.from_dict(polizaNueva)
		# Comprobar que el cliente es diferente tras la desactivación
		assert_that(polizaAntigua).is_not_equal_to(polizaNueva)
		# Comprobar que es el mismo DNI
		assert_that(polizaAntigua.get_id_poliza()).is_equal_to(polizaNueva.get_id_poliza())

# Test de subir prescripcion
def test_subir_prescripcion():
	controlador = Controller()
	# Creación de usuario cliente
	cliente = UsuarioCliente("Marcos", "marcos@gmail.com", "28394819-T", "ES9912345392003384830729")
	# Crear usuario cliente
	controlador.crear_usuario(cliente, 1)
	
	# Creación fecha
	fecha = datetime.datetime(2020, 5, 17)
	# Creación Póliza activa
	poliza = Poliza(cliente, cliente.get_dni(), fecha, TipoPoliza.Total, 9.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	# Crear Póliza
	controlador.crear_poliza(poliza)
	
	# Creación fecha
	fecha_realizacion = datetime.datetime(2020, 6, 22)
	# Creación prescripción con usuario y póliza
	prescripcion = Prescripcion(cliente.get_dni(), cliente, poliza.get_id_poliza(), fecha_realizacion, Especialidad.Epidemiologia, "D. Miguel", "D. Fernando", ["Serología", "PCR"], "Consulta 3")
	# Comprobar que en el controlador no existe la prescripción
	assert_that(controlador.mongo.db.prescripciones.find({'id_prescripcion': prescripcion.get_id_prescripcion()}).count()).is_equal_to(0)
	# Crear prescripción
	controlador.subir_prescripcion(prescripcion)
	# Comprobar que en el controlador ya sí existe la prescripción
	assert_that(controlador.mongo.db.prescripciones.find({'id_prescripcion': prescripcion.get_id_prescripcion()}).count()).is_equal_to(1)
	
# Test de solicitar autorización
def test_solicitar_autorizacion():
	controlador = Controller()
	# Creación de usuario cliente
	cliente = UsuarioCliente("Marta", "marta@gmail.com", "71238492-W", "ES9912341852003384000029")
	# Crear usuario cliente
	controlador.crear_usuario(cliente, 1)
	
	# Creación fecha
	fecha = datetime.datetime(2020,6,18)
	# Creación Póliza activa
	poliza = Poliza(cliente, cliente.get_dni(), fecha, TipoPoliza.Total, 13.99, 30.99, ["Serología"], [ModuloExtra.Dental], True)
	# Crear Póliza
	controlador.crear_poliza(poliza)
	
	# Creación fecha
	fecha_realizacion = datetime.datetime(2020, 6, 24)
	# Creación prescripción con usuario y póliza
	prescripcion = Prescripcion(cliente.get_dni(), cliente, poliza.get_id_poliza(), fecha_realizacion, Especialidad.Neurologia, "D. Miguel", "D. Fernando", ["TAC", "PCR"], "Consulta 3")
	# Crear prescripción
	controlador.subir_prescripcion(prescripcion)
	
	# Creación fecha
	fecha_realizacion = datetime.datetime(2020, 6, 24)
	# Creación autorización con usuario y póliza
	autorizacion = Autorizacion("AU-71238492-1", cliente, prescripcion.get_id_prescripcion(), poliza.get_id_poliza(), True, "", fecha_realizacion, Especialidad.Neurologia, ["TAC", "PCR"], "D. Fernando", "Consulta 3")
	# Comprobar que en el controlador no existe la autorización
	assert_that(controlador.mongo.db.autorizaciones.find({'id_autorizacion': autorizacion.get_id_autorizacion()}).count()).is_equal_to(0)
	# Crear autorización
	controlador.solicitar_autorizacion(prescripcion.get_id_prescripcion())
	# Comprobar que en el controlador ya sí existe la autorización
	assert_that(controlador.mongo.db.autorizaciones.find({'id_autorizacion': autorizacion.get_id_autorizacion()}).count()).is_equal_to(1)

# Test de crear autorización
def test_crear_autorizacion():
	controlador = Controller()
	# Creación de usuario cliente
	cliente = UsuarioCliente("Julio", "julio1@gmail.com", "77223418-R", "ES9912345811003387447729")
	# Crear usuario cliente
	controlador.crear_usuario(cliente, 1)
	
	# Creación fecha
	fecha = datetime.datetime(2020, 5, 17)
	# Creación Póliza activa
	poliza = Poliza(cliente, cliente.get_dni(), fecha, TipoPoliza.Total, 9.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	# Crear Póliza
	controlador.crear_poliza(poliza)

	# Creación fecha
	fecha_realizacion = datetime.datetime(2020, 6, 22)
	# Creación autorización con usuario y póliza
	autorizacion = Autorizacion(cliente.get_dni(), cliente, cliente.get_dni(), poliza.get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Miguel", "Consulta 3")
	# Comprobar que en el controlador no existe la autorización
	assert_that(controlador.mongo.db.autorizaciones.find({'id_autorizacion': autorizacion.get_id_autorizacion()}).count()).is_equal_to(0)
	# Crear autorización
	controlador.crear_autorizacion(autorizacion)
	# Comprobar que en el controlador ya sí existe la autorización
	assert_that(controlador.mongo.db.autorizaciones.find({'id_autorizacion': autorizacion.get_id_autorizacion()}).count()).is_equal_to(1)

# Test de modificar autorización
def test_modificar_autorizacion():
	controlador = Controller()
	# Obtener cliente por el DNI
	cliente = controlador.mongo.db.usuarios.find_one({'dni': '77223418-R'})
	# Obtener póliza por el ID
	poliza = controlador.mongo.db.usuarios.find_one({'id_poliza': 'MA-77223418-1'})
	
	if cliente != None and poliza != None:
		cliente = UsuarioCliente.from_dict(cliente)
		poliza = Poliza.from_dict(poliza)
		# Creación de fecha
		fecha_realizacion = datetime.datetime(2020, 6, 22)
		# Creación de autorización
		autorizacionAntigua = Autorizacion("AU-77223418-1", cliente, cliente.get_dni(), poliza.get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Miguel", "Consulta 3")
		# Modificar la autorización
		controlador.modificar_autorizacion(autorizacionAntigua.get_id_autorizacion(), "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Gustavo", "Consulta 3")
		# Obtengo la autorizacion almacenada
		autorizacionNueva = controlador.mongo.db.autorizaciones.find_one({'id_autorizacion': autorizacionAntigua.get_id_autorizacion()})
		autorizacionNueva = Autorizacion.from_dict(autorizacionNueva)
		# Comprobar que el cliente es diferente tras la modificación
		assert_that(autorizacionAntigua).is_not_equal_to(autorizacionNueva)
		# Comprobar que es el mismo DNI
		assert_that(autorizacionAntigua.get_id_autorizacion()).is_equal_to(autorizacionNueva.get_id_autorizacion())
			
# Test de consulta de autorización
def test_consultar_autorizacion():
	controlador = Controller()
	# Obtener cliente por el DNI
	cliente = controlador.mongo.db.usuarios.find_one({'dni': '77223418-R'})
	# Obtener póliza por el ID
	poliza = controlador.mongo.db.usuarios.find_one({'id_poliza': 'MA-77223418-1'})
	
	if cliente != None and poliza != None:
		cliente = UsuarioCliente.from_dict(cliente)
		poliza = Poliza.from_dict(poliza)
		# Creación de fecha
		fecha_realizacion = datetime.datetime(2020, 6, 22)
		# Creación de autorización
		autorizacion1 = Autorizacion("AU-77223418-1", cliente, cliente.get_dni(), poliza.get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Gustavo", "Consulta 3")
		# Consultar autorización del controlador con el ID de la autorización
		autorizacion2 = controlador.consultar_autorizacion("AU-77223418-1")
		# Comprobar que la autorización obtenida es igual, y por lo tanto la consulta es correcta
		assert_that(autorizacion1).is_equal_to(autorizacion2)
			
# Test de aprobar/denegar autorizacion
def test_aprobar_denegar_autorizacion():
	controlador = Controller()
	# Obtener cliente por el DNI
	cliente = controlador.mongo.db.usuarios.find_one({'dni': '77223418-R'})
	# Obtener póliza por el ID
	poliza = controlador.mongo.db.usuarios.find_one({'id_poliza': 'MA-77223418-1'})
	
	if cliente != None and poliza != None:
		cliente = UsuarioCliente.from_dict(cliente)
		poliza = Poliza.from_dict(poliza)
		# Creación de fecha
		fecha_realizacion = datetime.datetime(2020, 6, 22)
		# Creación de autorización
		autorizacionAntigua = Autorizacion("AU-77223418-1", cliente, cliente.get_dni(), poliza.get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Gustavo", "Consulta 3")
		# Denegar la autorización
		controlador.aprobar_denegar_autorizacion(autorizacionAntigua.get_id_autorizacion(), False, "Servicio no cubierto en póliza.")
		# Obtengo la autorizacion almacenada
		autorizacionNueva = controlador.mongo.db.autorizaciones.find_one({'id_autorizacion': autorizacionAntigua.get_id_autorizacion()})
		autorizacionNueva = Autorizacion.from_dict(autorizacionNueva)
		# Comprobar que el cliente es diferente tras la modificación
		assert_that(autorizacionAntigua).is_not_equal_to(autorizacionNueva)
		# Comprobar que es el mismo DNI
		assert_that(autorizacionAntigua.get_id_autorizacion()).is_equal_to(autorizacionNueva.get_id_autorizacion())

# Test de crear cita médica
def test_crear_cita():
	controlador = Controller()
	# Obtener autorización por el ID
	autorizacion = controlador.mongo.db.autorizaciones.find_one({'id_autorizacion': 'AU-77223418-1'})
	
	if autorizacion != None:
		autorizacion = Autorizacion.from_dict(autorizacion)
		# Aprobar la autorización
		controlador.aprobar_denegar_autorizacion(autorizacion.get_id_autorizacion(), True, "")
		
		# Creación hora
		hora = datetime.time(3, 45, 12)
		# Creación de cita
		cita = Cita(autorizacion.get_id_autorizacion(), autorizacion.get_asegurado(), autorizacion.get_id_prescripcion(), autorizacion.get_fecha_realizacion(), hora, autorizacion.get_facultativo_realizador(), autorizacion.get_consulta())
		# Comprobar que en el controlador no existe la cita
		assert_that(controlador.mongo.db.citas.find({'id_autorizacion': autorizacion.get_id_autorizacion()}).count()).is_equal_to(0)
		# Crear autorización
		controlador.crear_cita(cita)
		# Comprobar que en el controlador ya sí existe la cita
		assert_that(controlador.mongo.db.citas.find({'id_autorizacion': autorizacion.get_id_autorizacion()}).count()).is_equal_to(1)
				
# Test de modificar cita médica
def test_modificar_cita():
	controlador = Controller()
	# Obtener cita por el ID
	cita = controlador.mongo.db.citas.find_one({'id_autorizacion': 'AU-77223418-1'})
	
	if cita != None:
		cita = Cita.from_dict(cita)
		# Creación hora
		hora = datetime.time(3, 30, 11)
		# Creación de cita
		citaAntigua = Cita(cita.get_id_autorizacion(), cita.get_asegurado(), cita.get_id_prescripcion(), cita.get_fecha(), cita.get_hora(), cita.get_facultativo_realizador(), cita.get_consulta())
		# Modificar cita
		controlador.modificar_cita(citaAntigua.get_id_autorizacion(), cita.get_fecha(), hora, cita.get_facultativo_realizador(), cita.get_consulta())
		# Obtengo la cita almacenada
		citaNueva = controlador.mongo.db.citas.find_one({'id_autorizacion': citaAntigua.get_id_autorizacion()})
		citaNueva = Cita.from_dict(citaNueva)
		# Comprobar que el cita es diferente tras la modificación
		assert_that(citaAntigua).is_not_equal_to(citaNueva)
		# Comprobar que es el mismo DNI
		assert_that(citaAntigua.get_id_autorizacion()).is_equal_to(citaNueva.get_id_autorizacion())
			
# Test de consulta de cita médica
def test_consultar_cita():
	controlador = Controller()
	# Obtener cita por el ID
	cita = controlador.mongo.db.citas.find_one({'id_autorizacion': 'AU-77223418-1'})
	
	if cita != None:
		cita = Cita.from_dict(cita)
		# Creación de cita
		cita1 = Cita(cita.get_id_autorizacion(), cita.get_asegurado(), cita.get_id_prescripcion(), cita.get_fecha(), cita.get_hora(), cita.get_facultativo_realizador(), cita.get_consulta())
		# Consultar cita
		cita2 = controlador.consultar_cita("AU-77223418-1")
		# Comprobar que la cita obtenida es igual, y por lo tanto la consulta es correcta
		assert_that(cita1).is_equal_to(cita2)

# Test de consulta de usuario
def test_consultar_usuario():
	controlador = Controller()
	
	# Creación objeto UsuarioCliente
	usuario1 = UsuarioCliente("Julio", "julio1@gmail.com", "77223418-R", "ES9912345811003387447729")
	# Consultar usuario del controlador con el DNI del usuario asociado
	usuario2 = controlador.consultar_usuario("77223418-R")
	# Comprobar que el usuario obtenido es igual, y por lo tanto la consulta es correcta
	assert_that(usuario1).is_equal_to(usuario2)	

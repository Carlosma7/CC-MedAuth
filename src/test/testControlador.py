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
	adminOtro = UsuarioAdmin("Fernando", "fer@gmail.com", "12925767-F", "")
	
	# Crear administrador
	controlador.crear_usuario(admin, 0)
	# Comprobar que únicamente se ha insertado el usuario seleccionado
	assert_that(controlador.usuarios).contains(admin).does_not_contain(adminOtro)
	
# Test de creación de usuario cliente/asegurado
def test_crear_cliente():
	controlador = Controller()
	# Creación de usuario cliente
	cliente = UsuarioCliente("Juan", "juan@gmail.com", "75123540-F", "ES1234111892738495273849")
	clienteOtro = UsuarioCliente("Victor", "victor7ma@gmail.com", "71855223-F", "ES1234567812345678910231")
	
	# Crear cliente
	controlador.crear_usuario(cliente, 1)
	# Comprobar que únicamente se ha insertado el usuario seleccionado
	assert_that(controlador.usuarios).contains(cliente).does_not_contain(clienteOtro)
	
# Test de modificación de administrador
def test_modificar_admin():
	controlador = Controller()
	# Creación de usuario administrador
	adminAntiguo = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "")
	# Modificación de usuario administrador
	controlador.modificar_usuario(adminAntiguo, 'Carlos', 'charles@gmail.com', "")
	# Obtengo el usuario administrador almacenado
	adminNuevo = [a for a in controlador.usuarios if a.get_dni() == adminAntiguo.get_dni()]
	if len(adminNuevo) > 0:
		# Comprobar que el administrador es diferente tras la modificación
		assert_that(adminAntiguo).is_not_equal_to(adminNuevo[0])
		# Comprobar que es el mismo DNI
		assert_that(adminNuevo[0].get_dni()).is_equal_to(adminAntiguo.get_dni())

# Test de modificación de cliente
def test_modificar_cliente():
	controlador = Controller()
	# Creación de usuario cliente
	clienteAntiguo = UsuarioCliente("Juan", "juan@gmail.com", "75123540-F", "ES1234111892738495273849")
	# Modificación de usuario cliente
	controlador.modificar_usuario(clienteAntiguo, 'Juan', 'juan@gmail.com', "ES1298742874928365740192")
	# Obtengo el usuario cliente almacenado
	clienteNuevo = [a for a in controlador.usuarios if a.get_dni() == clienteAntiguo.get_dni()]
	if len(clienteNuevo) > 0:
		# Comprobar que el cliente es diferente tras la modificación
		assert_that(clienteAntiguo).is_not_equal_to(clienteNuevo[0])
		# Comprobar que es el mismo DNI
		assert_that(clienteNuevo[0].get_dni()).is_equal_to(clienteAntiguo.get_dni())

# Test de eliminar administración
def test_eliminar_admin():
	controlador = Controller()
	# Creación de usuario administrativo
	admin = UsuarioAdmin("Carlos", "charles@gmail.com", "75925767-F", "charles@medauth.com")
	# Comprobar que el usuario administrativo existe en el controlador
	assert_that(controlador.usuarios).contains(admin)
	# Eliminar el usuario administrativo
	controlador.eliminar_usuario(admin.get_dni())
	# Comprobar que el usuario administrativo ya no existe en el controlador
	assert_that(controlador.usuarios).does_not_contain(admin)

# Test de eliminar cliente
def test_eliminar_cliente():
	controlador = Controller()
	# Creación de usuario cliente
	cliente = UsuarioCliente("Juan", "juan@gmail.com", "75123540-F", "ES1298742874928365740192")
	# Comprobar que el usuario cliente existe en el controlador
	assert_that(controlador.usuarios).contains(cliente)
	# Eliminar el usuario cliente
	controlador.eliminar_usuario(cliente.get_dni())
	# Comprobar que el usuario cliente ya no existe en el controlador
	assert_that(controlador.usuarios).does_not_contain(cliente)

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
	assert_that(controlador.polizas).does_not_contain(p)
	# Crear póliza
	controlador.crear_poliza(p)
	# Comprobar que la póliza ya si existe en el controlador
	assert_that(controlador.polizas).contains(p)

# Test de modificación de póliza
def test_modificar_poliza():
	controlador = Controller()
	# Obtener cliente por el DNI
	cliente = [c for c in controlador.usuarios if c.get_dni() == "75125767-F"]
	
	if len(cliente) > 0:
		# Creación fecha
		fecha = datetime.datetime(2020, 5, 17)
		# Creación objeto Póliza
		polizaAntigua = Poliza(cliente[0], "MA-75125767-1", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		# Modificación de póliza
		controlador.modificar_poliza(polizaAntigua, fecha, TipoPoliza.Basica, 10.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental])
		# Obtener la póliza del controlador tras modificar
		polizaNueva = [a for a in controlador.polizas if a.get_titular().get_dni() == polizaAntigua.get_titular().get_dni()]
		if len(polizaNueva) > 0:
			# Comprobar que la póliza no es igual tras la modificación
			assert_that(polizaAntigua).is_not_equal_to(polizaNueva[0])
			# Comprobar que el ID de la póliza es el mismo
			assert_that(polizaAntigua.get_id_poliza()).is_equal_to(polizaNueva[0].get_id_poliza())


# Test de consulta de póliza
def test_consultar_poliza():
	controlador = Controller()
	# Obtener cliente por el DNI
	cliente = [c for c in controlador.usuarios if c.get_dni() == "75125767-F"]
	
	if len(cliente) > 0:
		# Creación fecha
		fecha = datetime.datetime(2020, 5, 17)
		# Creación objeto Póliza
		poliza1 = Poliza(cliente[0], "MA-75125767-1", fecha, TipoPoliza.Basica, 10.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		# Consultar póliza del controlador con el DNI del asegurado asociado
		poliza2 = controlador.consultar_poliza("75125767-F")
		# Comprobar que la póliza obtenida es igual, y por lo tanto la consulta es correcta
		assert_that(poliza1).is_equal_to(poliza2)

# Test de desactivar póliza
def test_desactivar_poliza():
	controlador = Controller()
	# Obtener cliente por el DNI
	cliente = [c for c in controlador.usuarios if c.get_dni() == "75125767-F"]
	
	if len(cliente) > 0:
		# Creación fecha
		fecha = datetime.datetime(2020, 5, 17)
		# Creación objeto Póliza activa
		polizaAntigua = Poliza(cliente[0], "MA-75125767-1", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		# Desactivación de la póliza
		controlador.desactivar_poliza(polizaAntigua.get_titular().get_dni())
		# Obtener la póliza del controlador tras desactivar
		polizaNueva = [a for a in controlador.polizas if a.get_titular().get_dni() == polizaAntigua.get_titular().get_dni()]
		if len(polizaNueva) > 0:
			# Comprobar que la póliza no es igual tras la desactivación
			assert_that(polizaAntigua).is_not_equal_to(polizaNueva[0])
			# Comprobar que el ID de la póliza es el mismo
			assert_that(polizaAntigua.get_id_poliza()).is_equal_to(polizaNueva[0].get_id_poliza())

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
	assert_that(controlador.prescripciones).does_not_contain(prescripcion)
	# Crear prescripción
	controlador.subir_prescripcion(prescripcion)
	# Comprobar que en el controlador ya sí existe la prescripción
	assert_that(controlador.prescripciones).contains(prescripcion)
	

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
	assert_that(controlador.autorizaciones).does_not_contain(autorizacion)
	# Crear autorización
	controlador.crear_autorizacion(autorizacion)
	# Comprobar que en el controlador ya sí existe la autorización
	assert_that(controlador.autorizaciones).contains(autorizacion)

# Test de modificar autorización
def test_modificar_autorizacion():
	controlador = Controller()
	# Obtener cliente por el DNI
	cliente = [c for c in controlador.usuarios if c.get_dni() == "77223418-R"]
	# Obtener póliza por el ID
	poliza = [p for p in controlador.polizas if p.get_id_poliza() == "MA-77223418-1"]
	
	if len(cliente) > 0 and len(poliza) > 0:
		# Creación de fecha
		fecha_realizacion = datetime.datetime(2020, 6, 22)
		# Creación de autorización
		autorizacionAntigua = Autorizacion("AU-77223418-1", cliente[0], cliente[0].get_dni(), poliza[0].get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Miguel", "Consulta 3")
		# Modificar la autorización
		controlador.modificar_autorizacion(autorizacionAntigua, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Gustavo", "Consulta 3")
		# Obtener la autorización del controlador
		autorizacionNueva = [a for a in controlador.autorizaciones if a.get_id_autorizacion() == autorizacionAntigua.get_id_autorizacion()]
		if len(autorizacionNueva) > 0:
			# Comprobar que la autorización no es igual tras la modificación
			assert_that(autorizacionAntigua).is_not_equal_to(autorizacionNueva[0])
			# Comprobar que el ID de la autorización es el mismo
			assert_that(autorizacionAntigua.get_id_autorizacion()).is_equal_to(autorizacionNueva[0].get_id_autorizacion())
			
# Test de consulta de autorización
def test_consultar_autorizacion():
	controlador = Controller()
	# Obtener cliente por el DNI
	cliente = [c for c in controlador.usuarios if c.get_dni() == "75125767-F"]
	# Obtener póliza por el ID
	poliza = [p for p in controlador.polizas if p.get_id_poliza() == "MA-77223418-1"]
	
	if len(cliente) > 0 and len(poliza) > 0:
		# Creación de fecha
		fecha_realizacion = datetime.datetime(2020, 6, 22)
		# Creación de autorización
		autorizacion1 = Autorizacion("AU-77223418-1", cliente[0], cliente[0].get_dni(), poliza[0].get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Gustavo", "Consulta 3")
		# Consultar autorización del controlador con el ID de la autorización
		autorizacion2 = controlador.consultar_autorizacion("AU-77223418-1")
		# Comprobar que la autorización obtenida es igual, y por lo tanto la consulta es correcta
		assert_that(autorizacion1).is_equal_to(autorizacion2)
			
# Test de aprobar/denegar autorizacion
def test_aprobar_denegar_autorizacion():
	controlador = Controller()
	# Obtener cliente por el DNI
	cliente = [c for c in controlador.usuarios if c.get_dni() == "77223418-R"]
	# Obtener póliza por el ID
	poliza = [p for p in controlador.polizas if p.get_id_poliza() == "MA-77223418-1"]
	
	if len(cliente) > 0 and len(poliza) > 0:
		# Creación de fecha
		fecha_realizacion = datetime.datetime(2020, 6, 22)
		# Creación de autorización
		autorizacionAntigua = Autorizacion("AU-77223418-1", cliente[0], cliente[0].get_dni(), poliza[0].get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Gustavo", "Consulta 3")
		# Denegar la autorización
		controlador.aprobar_denegar_autorizacion(autorizacionAntigua, False, "Servicio no cubierto en póliza.")
		# Obtener la autorización del controlador
		autorizacionNueva = [a for a in controlador.autorizaciones if a.get_id_autorizacion() == autorizacionAntigua.get_id_autorizacion()]
		if len(autorizacionNueva) > 0:
			# Comrpobar que la autorización no es igual tras la denegación
			assert_that(autorizacionAntigua).is_not_equal_to(autorizacionNueva[0])
			# Comprobar que el ID de la autorización es el mismo
			assert_that(autorizacionAntigua.get_id_autorizacion()).is_equal_to(autorizacionNueva[0].get_id_autorizacion())

# Test de crear cita médica
def test_crear_cita():
	controlador = Controller()
	# Obtener autorización por el ID
	autorizacion = [a for a in controlador.autorizaciones if a.get_id_poliza() == "AU-77223418-1"]
	
	if len(autorizacion) > 0:
		autorizacion = autorizacion[0]
		# Aprobar la autorización
		controlador.aprobar_denegar_autorizacion(autorizacion, True, "")
		
		# Creación hora
		hora = datetime.time(3, 45, 12)
		# Creación de cita
		cita = Cita(autorizacion.get_id_autorizacion(), autorizacion.get_asegurado(), autorizacion.get_id_prescripcion(), autorizacion.get_fecha_realizacion(), hora, autorizacion.get_facultativo_realizador(), autorizacion.get_consulta())
		
		# Comprobar que la cita no existe en el controlador
		assert_that(controlador.citas).does_not_contain(cita)
		# Crear cita
		controlador.crear_cita(cita)
		# Comprobar que la cita ya sí existe en el controlador
		assert_that(controlador.citas).contains(cita)
				
# Test de modificar cita médica
def test_modificar_cita():
	controlador = Controller()
	# Obtener autorización por el ID
	autorizacion = [a for a in controlador.autorizaciones if a.get_id_poliza() == "AU-77223418-1"]
	
	if len(autorizacion) > 0:
		# Creación hora
		hora = datetime.time(3, 30, 11)
		# Creación de cita
		citaAntigua = Cita(autorizacion.get_id_autorizacion(), autorizacion.get_asegurado(), autorizacion.get_id_prescripcion(), autorizacion.get_fecha_realizacion(), hora, autorizacion.get_facultativo_realizador(), autorizacion.get_consulta())
		# Modificar cita
		controlador.modificar_cita(citaAntigua, cita.get_fecha(), hora, cita.get_consulta())
		# Obtener cita del controlador
		citaNueva = [c for c in controlador.citas if c.get_id_autorizacion() == citaAntigua.get_id_autorizacion()]
		if len(citaNueva) > 0:
			# Comprobar que la cita no es igual tras la modificación
			assert_that(citaAntigua).is_not_equal_to(citaNueva[0])
			# Comprobar que el ID de la autorización es el mismo
			assert_that(citaAntigua.get_id_autorizacion()).is_equal_to(citaNueva[0].get_id_autorizacion())
			
# Test de consulta de cita médica
def test_consultar_cita():
	controlador = Controller()
	# Obtener autorización por el ID
	autorizacion = [a for a in controlador.autorizaciones if a.get_id_poliza() == "AU-77223418-1"]
	
	if len(autorizacion) > 0:
		# Creación hora
		hora = datetime.time(3, 30, 11)
		# Creación de cita
		cita1 = Cita(autorizacion.get_id_autorizacion(), autorizacion.get_asegurado(), autorizacion.get_id_prescripcion(), autorizacion.get_fecha_realizacion(), hora, autorizacion.get_facultativo_realizador(), autorizacion.get_consulta())
		# Consultar cita
		cita2 = controlador.consultar_cita("AU-77223418-1")
		# Comprobar que la cita obtenida es igual, y por lo tanto la consulta es correcta
		assert_that(cita1).is_equal_to(cita2)		

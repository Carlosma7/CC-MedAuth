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
	cliente = UsuarioCliente("Juan", "juan@gmail.com", "7512354-F", "ES12341118")
	clienteOtro = UsuarioCliente("Victor", "victor7ma@gmail.com", "71855223-F", "ES12345678")
	
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
	controlador.modificar_usuario(adminAntiguo, 'Carlos', 'charles@gmail.com')
	# Obtengo el usuario administrador almacenado
	adminNuevo = [a for a in controlador.usuarios if a.get_dni() == adminAntiguo.get_dni()]
	if len(adminNuevo) > 0:
		# Comprobar que el administrador es diferente tras la modificación
		assert_that(adminAntiguo).is_not_equal_to(adminNuevo[0])
		# Comprobar que es el mismo DNI
		assert_that(adminNuevo[0].get_dni()).is_equal_to(adminAntiguo[0].get_dni())

# Test de modificación de cliente
def test_modificar_cliente():
	controlador = Controller()
	# Creación de usuario cliente
	clienteAntiguo = UsuarioCliente("Juan", "juan@gmail.com", "7512354-F", "ES12341118")
	# Modificación de usuario cliente
	controlador.modificar_usuario(clienteAntiguo, 'Juan', 'juan@gmail.com', "ES12987428")
	# Obtengo el usuario cliente almacenado
	clienteNuevo = [a for a in controlador.usuarios if a.get_dni() == clienteAntiguo.get_dni()]
	if len(clienteNuevo) > 0:
		# Comprobar que el cliente es diferente tras la modificación
		assert_that(clienteAntiguo).is_not_equal_to(clienteNuevo[0])
		# Comprobar que es el mismo DNI
		assert_that(clienteNuevo[0].get_dni()).is_equal_to(clienteAntiguo[0].get_dni())

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
	cliente = UsuarioCliente("Juan", "juan@gmail.com", "7512354-F", "ES12987428")
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
	cliente = UsuarioCliente("Alejandro", "alex@gmail.com", "75125767-F", "ES99345678")
	# Crear cliente
	controlador.crear_usuario(cliente)

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
			# Comprobar que el ID de la pñoliza es el mismo
			assert_that(polizaAntigua.get_id_poliza()).is_equal_to(polizaNueva[0].get_id_poliza())

# Test de crear autorización
def test_crear_autorizacion():
	controlador = Controller()
	# Creación de usuario cliente
	cliente = UsuarioCliente("Julio", "julio1@gmail.com", "777223418-R", "ES99123458")
	# Crear usuario cliente
	controlador.crear_usuario(cliente)
	
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
	cliente = [c for c in controlador.usuariosClientes if c.get_dni() == "777223418-R"]
	poliza = [p for p in controlador.polizas if p.get_id_poliza() == "MA-777223418-1"]
	
	if len(cliente) > 0 and len(poliza) > 0:
		fecha_realizacion = datetime.datetime(2020, 6, 22)
		autorizacionAntigua = Autorizacion("AU-777223418-1", cliente[0], cliente[0].get_dni(), poliza[0].get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Miguel", "Consulta 3")
		controlador.modificar_autorizacion(autorizacionAntigua, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Gustavo", "Consulta 3")
		autorizacionNueva = [a for a in controlador.autorizaciones if a.get_id_autorizacion() == autorizacionAntigua.get_id_autorizacion()]
		if len(autorizacionNueva) > 0:
			assert_that(autorizacionAntigua).is_not_equal_to(autorizacionNueva[0])
			
# Test de consulta de autorización
def test_consultar_autorizacion():
	controlador = Controller()
	cliente = [c for c in controlador.usuariosClientes if c.get_dni() == "75125767-F"]
	poliza = [p for p in controlador.polizas if p.get_id_poliza() == "MA-777223418-1"]
	
	if len(cliente) > 0 and len(poliza) > 0:
		fecha_realizacion = datetime.datetime(2020, 6, 22)
		autorizacion1 = Autorizacion("AU-777223418-1", cliente[0], cliente[0].get_dni(), poliza[0].get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Gustavo", "Consulta 3")
		autorizacion2 = controlador.consultar_autorizacion("AU-777223418-1")
		assert_that(autorizacion1).is_equal_to(autorizacion2)
			
# Test de aprobar/denegar autorizacion
def test_aprobar_denegar_autorizacion():
	controlador = Controller()
	cliente = [c for c in controlador.usuariosClientes if c.get_dni() == "777223418-R"]
	poliza = [p for p in controlador.polizas if p.get_id_poliza() == "MA-777223418-1"]
	
	if len(cliente) > 0 and len(poliza) > 0:
		fecha_realizacion = datetime.datetime(2020, 6, 22)
		autorizacionAntigua = Autorizacion("AU-777223418-1", cliente[0], cliente[0].get_dni(), poliza[0].get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Gustavo", "Consulta 3")
		controlador.aprobar_denegar_autorizacion(autorizacionAntigua, False, "Servicio no cubierto en póliza.")
		autorizacionNueva = [a for a in controlador.autorizaciones if a.get_id_autorizacion() == autorizacionAntigua.get_id_autorizacion()]
		if len(autorizacionNueva) > 0:
			assert_that(autorizacionAntigua).is_not_equal_to(autorizacionNueva[0])

# Test de crear cita médica
def test_crear_cita():
	controlador = Controller()
	autorizacion = [a for a in controlador.autorizaciones if a.get_id_poliza() == "AU-777223418-1"]
	
	if len(autorizacion) > 0:
		autorizacion = autorizacion[0]
		controlador.aprobar_denegar_autorizacion(autorizacion, True, "")
		
		hora = datetime.time(3, 45, 12)
		cita = Cita(autorizacion.get_id_autorizacion(), autorizacion.get_asegurado(), autorizacion.get_id_prescripcion(), autorizacion.get_fecha_realizacion(), hora, autorizacion.get_facultativo_realizador(), autorizacion.get_consulta())
		
		assert_that(controlador.citas).does_not_contain(cita)
		controlador.crear_cita(cita)
		assert_that(controlador.citas).contains(cita)
				
# Test de modificar cita médica
def test_modificar_cita():
	controlador = Controller()
	autorizacion = [a for a in controlador.autorizaciones if a.get_id_poliza() == "AU-777223418-1"]
	
	if len(autorizacion) > 0:
		hora = datetime.time(3, 30, 11)
		citaAntigua = Cita(autorizacion.get_id_autorizacion(), autorizacion.get_asegurado(), autorizacion.get_id_prescripcion(), autorizacion.get_fecha_realizacion(), hora, autorizacion.get_facultativo_realizador(), autorizacion.get_consulta())
		controlador.modificar_cita(citaAntigua, cita.get_fecha(), hora, cita.get_consulta())
		citaNueva = [c for c in controlador.citas if c.get_id_autorizacion() == citaAntigua.get_id_autorizacion()]
		if len(citaNueva) > 0:
			assert_that(citaAntigua).is_not_equal_to(citaNueva[0])		
			
# Test de consulta de cita médica
def test_consultar_cita():
	controlador = Controller()
	autorizacion = [a for a in controlador.autorizaciones if a.get_id_poliza() == "AU-777223418-1"]
	
	if len(autorizacion) > 0:
		hora = datetime.time(3, 30, 11)
		cita1 = Cita(autorizacion.get_id_autorizacion(), autorizacion.get_asegurado(), autorizacion.get_id_prescripcion(), autorizacion.get_fecha_realizacion(), hora, autorizacion.get_facultativo_realizador(), autorizacion.get_consulta())
		cita2 = controlador.consultar_cita("AU-777223418-1")
		assert_that(cita1).is_equal_to(cita2)		

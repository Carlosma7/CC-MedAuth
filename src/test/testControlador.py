import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from controlador import *

import pytest
from assertpy import assert_that

# Test de creación de usuario administrativo
def test_crear_admin():
	controlador = Controller()
	admin = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "")
	adminOtro = UsuarioAdmin("Fernando", "fer@gmail.com", "12925767-F", "")
	
	controlador.crear_admin(admin)
	assert_that(controlador.usuariosAdmins).contains(admin).does_not_contain(adminOtro)
	
# Test de creación de usuario cliente/asegurado
def test_crear_cliente():
	controlador = Controller()
	cliente = UsuarioCliente("Juan", "juan@gmail.com", "7512354-F", "ES12341118")
	clienteOtro = UsuarioCliente("Victor", "victor7ma@gmail.com", "71855223-F", "ES12345678")
	
	controlador.crear_cliente(cliente)
	assert_that(controlador.usuariosClientes).contains(cliente).does_not_contain(clienteOtro)
	
# Test de modificación de administrador
def test_modificar_admin():
	controlador = Controller()
	adminAntiguo = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "")
	controlador.modificar_admin(adminAntiguo, 'Carlos', 'charles@gmail.com')
	adminNuevo = [a for a in controlador.usuariosAdmins if a.get_dni() == adminAntiguo.get_dni()]
	if len(adminNuevo) > 0:
		assert_that(adminAntiguo).is_not_equal_to(adminNuevo[0])

# Test de modificación de cliente
def test_modificar_cliente():
	controlador = Controller()
	clienteAntiguo = UsuarioCliente("Juan", "juan@gmail.com", "7512354-F", "ES12341118")
	controlador.modificar_cliente(clienteAntiguo, 'Juan', 'juan@gmail.com', "ES12987428")
	clienteNuevo = [a for a in controlador.usuariosClientes if a.get_dni() == clienteAntiguo.get_dni()]
	if len(clienteNuevo) > 0:
		assert_that(clienteAntiguo).is_not_equal_to(clienteNuevo[0])

# Test de eliminar administración
def test_eliminar_admin():
	controlador = Controller()
	admin = UsuarioAdmin("Carlos", "charles@gmail.com", "75925767-F", "charles@medauth.com")
	assert_that(controlador.usuariosAdmins).contains(admin)
	controlador.eliminar_admin(admin.get_dni())
	assert_that(controlador.usuariosAdmins).does_not_contain(admin)

# Test de eliminar cliente
def test_eliminar_cliente():
	controlador = Controller()
	cliente = UsuarioCliente("Juan", "juan@gmail.com", "7512354-F", "ES12987428")
	assert_that(controlador.usuariosClientes).contains(cliente)
	controlador.eliminar_cliente(cliente.get_dni())
	assert_that(controlador.usuariosClientes).does_not_contain(cliente)

# Test de creación de póliza
def test_crear_poliza():
	controlador = Controller()
	cliente = UsuarioCliente("Alejandro", "alex@gmail.com", "75125767-F", "ES99345678")
	controlador.crear_cliente(cliente)

	fecha = datetime.datetime(2020, 5, 17)
	p = Poliza(cliente, cliente.get_dni(), fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	assert_that(controlador.polizas).does_not_contain(p)
	controlador.crear_poliza(p)
	assert_that(controlador.polizas).contains(p)

# Test de modificación de póliza
def test_modificar_poliza():
	controlador = Controller()
	cliente = [c for c in controlador.usuariosClientes if c.get_dni() == "75125767-F"]
	
	if len(cliente) > 0:
		fecha = datetime.datetime(2020, 5, 17)
		polizaAntigua = Poliza(cliente[0], "MA-75125767-1", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		controlador.modificar_poliza(polizaAntigua, fecha, TipoPoliza.Basica, 10.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental])
		polizaNueva = [a for a in controlador.polizas if a.get_titular().get_dni() == polizaAntigua.get_titular().get_dni()]
		if len(polizaNueva) > 0:
			assert_that(polizaAntigua).is_not_equal_to(polizaNueva[0])


# Test de consulta de póliza
def test_consultar_poliza():
	controlador = Controller()
	cliente = [c for c in controlador.usuariosClientes if c.get_dni() == "75125767-F"]
	
	if len(cliente) > 0:
		fecha = datetime.datetime(2020, 5, 17)
		poliza1 = Poliza(cliente[0], "MA-75125767-1", fecha, TipoPoliza.Basica, 10.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		poliza2 = controlador.consultar_poliza("75125767-F")
		assert_that(poliza1).is_equal_to(poliza2)

# Test de desactivar póliza
def test_desactivar_poliza():
	controlador = Controller()
	cliente = [c for c in controlador.usuariosClientes if c.get_dni() == "75125767-F"]
	
	if len(cliente) > 0:
		fecha = datetime.datetime(2020, 5, 17)
		polizaAntigua = Poliza(cliente[0], "MA-75125767-1", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		controlador.desactivar_poliza(polizaAntigua.get_titular().get_dni())
		polizaNueva = [a for a in controlador.polizas if a.get_titular().get_dni() == polizaAntigua.get_titular().get_dni()]
		if len(polizaNueva) > 0:
			assert_that(polizaAntigua).is_not_equal_to(polizaNueva[0])

# Test de crear autorización
def test_crear_autorizacion():
	controlador = Controller()
	cliente = UsuarioCliente("Julio", "julio1@gmail.com", "777223418-R", "ES99123458")
	controlador.crear_cliente(cliente)
	
	fecha = datetime.datetime(2020, 5, 17)
	poliza = Poliza(cliente, cliente.get_dni(), fecha, TipoPoliza.Total, 9.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	controlador.crear_poliza(poliza)

	fecha_realizacion = datetime.datetime(2020, 6, 22)
	autorizacion = Autorizacion(cliente.get_dni(), cliente, cliente.get_dni(), poliza.get_id_poliza(), True, "", fecha_realizacion, Especialidad.Epidemiologia, ["PCR"], "D. Miguel", "Consulta 3")
	assert_that(controlador.autorizaciones).does_not_contain(autorizacion)
	controlador.crear_autorizacion(autorizacion)
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
		autorizacionNueva = [a for a in controlador.autorizaciones if a.get_asegurado().get_dni() == autorizacionAntigua.get_asegurado().get_dni()]
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
		autorizacionNueva = [a for a in controlador.autorizaciones if a.get_asegurado().get_dni() == autorizacionAntigua.get_asegurado().get_dni()]
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

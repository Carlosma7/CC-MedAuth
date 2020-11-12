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


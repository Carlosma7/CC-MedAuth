import sys
import os
sys.path.append(os.path.abspath('./src/core/'))

from controlador import *
import datetime

if __name__ == '__main__':
	controlador = Controller()
	
	# [HU1] Creación usuario administrativo
	admin = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "")
	controlador.crear_admin(admin)
	
	# [HU2] Creación usuario asegurado
	cliente = UsuarioCliente("Juan", "juan@gmail.com", "7512354-F", "ES12341118")
	controlador.crear_cliente(cliente)

	# [HU3] Administrar usuario: Modificación administrador
	adminAntiguo = UsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "")
	controlador.modificar_admin(adminAntiguo, 'Carlos', 'charles@gmail.com')
	
	# [HU3] Administrar usuario: Modificación cliente
	clienteAntiguo = UsuarioCliente("Juan", "juan@gmail.com", "7512354-F", "ES12341118")
	controlador.modificar_cliente(clienteAntiguo, 'Juan', 'juan@gmail.com', "ES12987428")
	
	# [HU3] Administrar usuario: Eliminar usuario administrador
	admin = UsuarioAdmin("Carlos", "charles@gmail.com", "75925767-F", "charles@medauth.com")
	controlador.eliminar_admin(admin.get_dni())

	# [HU3] Administrar usuario: Eliminar usuario
	cliente = UsuarioCliente("Juan", "juan@gmail.com", "7512354-F", "ES12987428")
	controlador.eliminar_cliente(cliente.get_dni())
	
	# [HU4] Administrar póliza: Crear una póliza
	cliente = UsuarioCliente("Alejandro", "alex@gmail.com", "75125767-F", "ES99345678")
	controlador.crear_cliente(cliente)
	fecha = datetime.datetime(2020, 5, 17)
	p = Poliza(cliente, cliente.get_dni(), fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
	controlador.crear_poliza(p)
	
	# [HU4] Administrar póliza: Modificar una póliza
	cliente = [c for c in controlador.usuariosClientes if c.get_dni() == "75125767-F"]
	fecha = datetime.datetime(2020, 5, 17)
	
	if len(cliente) > 0:
		polizaAntigua = Poliza(cliente[0], "MA-75125767-1", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		controlador.modificar_poliza(polizaAntigua, fecha, TipoPoliza.Basica, 10.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental])
	
	# [HU5] Consultar póliza
	cliente = [c for c in controlador.usuariosClientes if c.get_dni() == "75125767-F"]
	fecha = datetime.datetime(2020, 5, 17)
	
	if len(cliente) > 0:
		poliza = controlador.consultar_poliza("75125767-F")
	
	# [HU4] Administrar póliza: Desactivar una póliza
	cliente = [c for c in controlador.usuariosClientes if c.get_dni() == "75125767-F"]
	fecha = datetime.datetime(2020, 5, 17)
	
	if len(cliente) > 0:
		polizaAntigua = Poliza(cliente[0], "MA-75125767-1", fecha, TipoPoliza.Basica, 5.99, 50.99, ["TAC", "Apendicitis"], [ModuloExtra.Dental], True)
		controlador.desactivar_poliza(polizaAntigua.get_titular().get_dni())

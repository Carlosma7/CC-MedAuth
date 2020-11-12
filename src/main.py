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

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

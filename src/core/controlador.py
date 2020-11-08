from modelos import *
from typing import List


# Clase controladora de lógica de negocio
class Controller:

	# Lista de entidades
	usuarios: List[Usuario] = []
	
	# [HU1] Creación usuario administrativo
	def crear_admin(self, nombre: str, email: str, dni: str):
		# Patrón correo: email@medauth
		email_empresarial = email.split('@')[0] + '@medauth.com'

		# Se crea el usuario administrativo
		c = TestUsuarioAdmin(nombre, email, dni, email_empresarial)

		# Se almacena
		self.usuarios.append(c)

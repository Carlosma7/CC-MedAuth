from modelos import *
from typing import List


class Controller:

	usuarios: List[Usuario] = []
	
	# [HU1] Creación usuario administrativo
	def crear_admin(self, nombre: str, email: str, dni: str):
		email_empresarial = email.split('@')[0] + '@medauth.com'

		c = UsuarioAdmin(nombre, email, dni, email_empresarial)
		self.usuarios.append(c)

	# [HU2] Creación usuario asegurado
	def crear_cliente(self, nombre: str, email: str, dni: str, cuenta_bancaria: str):
		c = UsuarioCliente(nombre, email, dni, cuenta_bancaria, 'a')
		self.usuarios.append(c)

	# [HU3] Administrar usuario: Modificación administrador
	def modificar_admin(self, nombre: str, email: str, dni: str):
		admin = [c for c in self.usuarios if c.dni == dni][0]
		admin.nombre = nombre
		admin.email = email

	# [HU3] Administrar usuario: Modificación cliente
	def modificar_cliente(self, nombre: str, email: str, dni: str, cuenta_bancaria: str):
		cliente = [c for c in self.usuarios if c.dni == dni][0]
		cliente.nombre = nombre
		cliente.email = email
		cliente.cuenta_bancaria = cuenta_bancaria

	# [HU3] Administrar usuario: Eliminar usuario
	def eliminar_usuario(self, dni: str):
		usuario = [c for c in self.usuarios if c.dni == dni][0]
		self.usuarios.remove(usuario)

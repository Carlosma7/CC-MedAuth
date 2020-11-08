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

	# [HU2] Creación usuario asegurado
	def crear_cliente(self, nombre: str, email: str, dni: str, cuenta_bancaria: str):
		# Se crea el usuario cliente/asegurado
		c = TestUsuarioCliente(nombre, email, dni, cuenta_bancaria, 'a')

		# Se almacena
		self.usuarios.append(c)

	# [HU3] Administrar usuario: Modificación administrador
	def modificar_admin(self, nombre: str, email: str, dni: str):
		# Se obtiene el usuario administrativo por su dni
		admin = [c for c in self.usuarios if c.get_dni() == dni][0]
		
		# Se modifica la información
		admin.set_nombre(nombre)
		admin.set_email(email)
		email_empresarial = email.split('@')[0] + '@medauth.com'
		admin.set_email_empresarial(email_empresarial)

	# [HU3] Administrar usuario: Modificación cliente
	def modificar_cliente(self, nombre: str, email: str, dni: str, cuenta_bancaria: str):
		# Se obtiene el usuario cliente/asegurado por su dni
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		
		# Se modifica la información
		cliente.set_nombre(nombre)
		cliente.set_email(email)
		cliente.set_cuenta_bancaria(cuenta_bancaria)
	
	# [HU3] Administrar usuario: Eliminar usuario
	def eliminar_usuario(self, dni: str):
		# Se obtiene el usuario por su dni
		usuario = [c for c in self.usuarios if c.get_dni() == dni][0]

		# Se elimina el usuario
		self.usuarios.remove(usuario)
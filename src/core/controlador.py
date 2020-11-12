from usuarioAdmin import UsuarioAdmin
from usuarioCliente import UsuarioCliente

from typing import List

# Clase controladora de lógica de negocio
class Controller:

	# Lista de entidades
	usuariosAdmins: List[UsuarioAdmin] = []
	usuariosClientes: List[UsuarioCliente] = []
	
	# [HU1] Creación usuario administrativo
	def crear_admin(self, admin: UsuarioAdmin):
		adm = [a for a in self.usuariosAdmins if a.get_dni() == admin.get_dni()]

		if len(adm) == 0:
			# Patrón correo: email@medauth
			email_empresarial = admin.get_email().split('@')[0] + '@medauth.com'

			# Se crea el usuario administrativo
			admin.set_email_empresarial(email_empresarial)

			# Se almacena
			self.usuariosAdmins.append(admin)

	# [HU2] Creación usuario asegurado
	def crear_cliente(self, cliente: UsuarioCliente):
		cli = [c for c in self.usuariosClientes if c.get_dni() == cliente.get_dni()]

		if len(cli) == 0:
			# Se crea el usuario cliente/asegurado
			self.usuariosClientes.append(cliente)

	# [HU3] Administrar usuario: Modificación administrador
	def modificar_admin(self, admin: UsuarioAdmin, nombre: str, email: str):
		# Se obtiene el usuario administrativo por su dni
		usuario = [c for c in self.usuariosAdmins if c.get_dni() == admin.get_dni()]

		if len(usuario) > 0:
			usuario = usuario[0]
			# Se modifica la información
			usuario.set_nombre(nombre)
			usuario.set_email(email)
			email_empresarial = email.split('@')[0] + '@medauth.com'
			usuario.set_email_empresarial(email_empresarial)

	# [HU3] Administrar usuario: Modificación cliente
	def modificar_cliente(self, cliente: UsuarioCliente, nombre: str, email: str, cuenta_bancaria: str):
		# Se obtiene el usuario cliente/asegurado por su dni
		usuario = [c for c in self.usuariosClientes if c.get_dni() == cliente.get_dni()]
		
		if len(usuario) > 0:
			usuario = usuario[0]
			# Se modifica la información
			usuario.set_nombre(nombre)
			usuario.set_email(email)
			usuario.set_cuenta_bancaria(cuenta_bancaria)

	# [HU3] Administrar usuario: Eliminar administrador
	def eliminar_admin(self, dni: str):
		admin_buscado = [c for c in self.usuariosAdmins if c.get_dni() == dni]

		if len(admin_buscado) > 0:
			# Se elimina el usuario
			self.usuariosAdmins.remove(admin_buscado[0])

	# [HU3] Administrar usuario: Eliminar cliente
	def eliminar_cliente(self, dni: str):
		cliente_buscado = [c for c in self.usuariosClientes if c.get_dni() == dni]

		if len(cliente_buscado) > 0:
			# Se elimina el usuario
			self.usuariosClientes.remove(cliente_buscado[0])

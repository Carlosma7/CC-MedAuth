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

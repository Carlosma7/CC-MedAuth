from usuarioAdmin import UsuarioAdmin

from typing import List

# Clase controladora de lógica de negocio
class Controller:

	# Lista de entidades
	usuariosAdmins: List[UsuarioAdmin] = []
	
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

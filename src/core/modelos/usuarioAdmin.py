from .usuario import Usuario


class UsuarioAdmin(Usuario):
	def __init__(self, nombre: str, email: str, dni: str, email_empresarial: str):
		self.nombre = nombre
		self.email = email
		self.dni = dni
		self.email_empresarial = email_empresarial
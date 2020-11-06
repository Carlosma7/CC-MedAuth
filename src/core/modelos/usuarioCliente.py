from .usuario import Usuario


class UsuarioCliente(Usuario):
	def __init__(self, nombre: str, email: str, dni: str, cuenta_bancaria: str, id_poliza: str):
		self.nombre = nombre
		self.email = email
		self.dni = dni
		self.cuenta_bancaria = cuenta_bancaria
		self.id_poliza = id_poliza
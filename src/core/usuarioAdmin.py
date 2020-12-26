from usuario import Usuario

# Clase de usuario administrativo
class UsuarioAdmin(Usuario):
	def __init__(self, nombre: str, email: str, dni: str, email_empresarial: str):
		self.__email_empresarial = email_empresarial
		super().__init__(nombre, email, dni, 0)
	
	# Métodos get/set
	def get_email_empresarial(self):
		return self.__email_empresarial
	
	def set_email_empresarial(self, email_empresarial: str):
		self.__email_empresarial = email_empresarial
	
	# Override método equal
	def __eq__(self, otra):
		return super().__eq__(otra) and (self.__email_empresarial == otra.get_email_empresarial())
	
	# Método para transformar objeto en un dict
	def to_dict(self):
		return {'nombre': super().get_nombre(), 'email': super().get_email(), 'dni': super().get_dni(), 'email_empresarial': self.__email_empresarial}

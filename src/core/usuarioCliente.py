from usuario import Usuario

# Clase de usuario cliente/asegurado
class UsuarioCliente(Usuario):
	def __init__(self, nombre: str, email: str, dni: str, cuenta_bancaria: str):
		self.__cuenta_bancaria = cuenta_bancaria
		super().__init__(nombre, email, dni)
	
	# Métodos get/set
	def get_cuenta_bancaria(self):
		return self.__cuenta_bancaria
		
	def set_cuenta_bancaria(self, cuenta_bancaria: str):
		self.__cuenta_bancaria = cuenta_bancaria
	
	# Override método equal
	def __eq__(self, otra):
		return super().__eq__(otra) and (self.__cuenta_bancaria == otra.get_cuenta_bancaria())

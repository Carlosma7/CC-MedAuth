# Clase de usuario cliente/asegurado
class UsuarioCliente():
	def __init__(self, nombre: str, email: str, dni: str, cuenta_bancaria: str):
		self.__nombre = nombre
		self.__email = email
		self.__dni = dni
		self.__cuenta_bancaria = cuenta_bancaria
	
	# Métodos get/set
	def get_nombre(self):
		return self.__nombre
		
	def set_nombre(self, nombre: str):
		self.__nombre = nombre
		
	def get_email(self):
		return self.__email
		
	def set_email(self, email: str):
		self.__email = email
	
	def get_dni(self):
		return self.__dni
		
	def get_cuenta_bancaria(self):
		return self.__cuenta_bancaria
		
	def set_cuenta_bancaria(self, cuenta_bancaria: str):
		self.__cuenta_bancaria = cuenta_bancaria
	
	# Override método equal
	def __eq__(self, otra):
		return (self.__nombre == otra.get_nombre() ) and (self.__email == otra.get_email()) and (self.__dni == otra.get_dni()) and (self.__cuenta_bancaria == otra.get_cuenta_bancaria())

# Clase de usuario
class Usuario():
	def __init__(self, nombre: str, email: str, dni: str, tipo: int):
		self.__nombre = nombre
		self.__email = email
		self.__dni = dni
		self.__tipo = tipo
	
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
	
	def get_tipo(self):
		return self.__tipo
	
	# Override método equal
	def __eq__(self, otra):
		return (self.__nombre == otra.get_nombre() ) and (self.__email == otra.get_email()) and (self.__dni == otra.get_dni()) and (self.__tipo == otra.get_tipo())

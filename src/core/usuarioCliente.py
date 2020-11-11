from .usuario import Usuario

# Clase de usuario cliente/asegurado
class UsuarioCliente(Usuario):
	def __init__(self, nombre: str, email: str, dni: str, cuenta_bancaria: str, id_poliza: str):
		self.__nombre = nombre
		self.__email = email
		self.__dni = dni
		self.__cuenta_bancaria = cuenta_bancaria
		self.__id_poliza = id_poliza
	
	# Métodos get/set
	def get_nombre(self):
		return self.__nombre
		
	def set_nombre(self, nombre):
		self.__nombre = nombre
		
	def get_email(self):
		return self.__email
		
	def set_email(self, email):
		self.__email = email
	
	def get_dni(self):
		return self.__dni
		
	def get_cuenta_bancaria(self):
		return self.__cuenta_bancaria
		
	def set_cuenta_bancaria(self, cuenta_bancaria):
		self.__cuenta_bancaria = cuenta_bancaria
		
	def get_id_poliza(self):
		return self.__id_poliza
	
	def set_id_poliza(self, id_poliza):
		self.__id_poliza = id_poliza
	
	# Override método equal
	def __eq__(self, otra):
		return (self.__nombre == otra.get_nombre() ) and (self.__email == otra.get_email()) and (self.__dni == otra.get_dni()) and (self.__cuenta_bancaria == otra.get_cuenta_bancaria() and (self.__id_poliza == otra.get_id_poliza()))
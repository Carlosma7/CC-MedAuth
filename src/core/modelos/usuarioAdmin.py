from .Usuario import TestUsuario

# Clase de usuario administrativo
class UsuarioAdmin(Usuario):
	def __init__(self, nombre: str, email: str, dni: str, email_empresarial: str):
		self.__nombre = nombre
		self.__email = email
		self.__dni = dni
		self.__email_empresarial = email_empresarial
	
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
		
	def get_email_empresarial(self):
		return self.__email_empresarial
	
	def set_email_empresarial(self, email_empresarial):
		self.__email_empresarial = email_empresarial
	
	# Override método equal
	def __eq__(self, otra):
		return (self.__nombre == otra.get_nombre() ) and (self.__email == otra.get_email()) and (self.__dni == otra.get_dni()) and (self.__email_empresarial == otra.get_email_empresarial())
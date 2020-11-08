from .testUsuario import TestUsuario
import pytest

# Clase de usuario administrativo
class TestUsuarioAdmin(TestUsuario):
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
		assert self.__nombre == otra.get_nombre()
		assert self.__email == otra.get_email()
		assert self.__dni == otra.get_dni()
		assert self.__email_empresarial == otra.get_email_empresarial()
		
		return (self.__nombre == otra.get_nombre() ) and (self.__email == otra.get_email()) and (self.__dni == otra.get_dni()) and (self.__email_empresarial == otra.get_email_empresarial())

# Test comparación usuario administrativo
def test_compare_usuario_admin():
	t1 = TestUsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "carlos@medauth.com")
	t2 = TestUsuarioAdmin("Carlos", "carlos7ma@gmail.com", "75925767-F", "carlos@medauth.com")
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test

from .testUsuario import TestUsuario
import pytest


class TestUsuarioCliente(TestUsuario):
	def __init__(self, nombre: str, email: str, dni: str, cuenta_bancaria: str, id_poliza: str):
		self.__nombre = nombre
		self.__email = email
		self.__dni = dni
		self.__cuenta_bancaria = cuenta_bancaria
		self.__id_poliza = id_poliza
		
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
	
	def __eq__(self, otra):
		assert self.__nombre == otra.get_nombre()
		assert self.__email == otra.get_email()
		assert self.__dni == otra.get_dni()
		assert self.__cuenta_bancaria == otra.get_cuenta_bancaria()
		assert self.__id_poliza == otra.get_id_poliza()
		
		return (self.__nombre == otra.get_nombre() ) and (self.__email == otra.get_email()) and (self.__dni == otra.get_dni()) and (self.__cuenta_bancaria == otra.get_cuenta_bancaria() and (self.__id_poliza == otra.get_id_poliza()))

def test_compare_usuario_cliente():
	t1 = TestUsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	t2 = TestUsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	t3 = TestUsuarioCliente("Carlos", "prueba@gmail.com", "75925767-F", "ES12345678", "12345678")
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test
	assert t2 == t3 # No pasa test

from modelos import *
from typing import List
import pytest


class TestController:

	usuarios: List[TestUsuario] = []
	
	# [HU1] Creación usuario administrativo
	def crear_admin(self, nombre: str, email: str, dni: str):
		email_empresarial = email.split('@')[0] + '@medauth.com'
		c = TestUsuarioAdmin(nombre, email, dni, email_empresarial)
		len_antes = len(self.usuarios)
		self.usuarios.append(c)
		assert len(self.usuarios) > len_antes
		
		admin = [a for a in self.usuarios if a.get_dni() == dni][0]
		assert admin.get_nombre() == nombre
		assert admin.get_email() == email
		assert admin.get_email_empresarial() == email_empresarial
	
	# [HU2] Creación usuario asegurado
	def crear_cliente(self, nombre: str, email: str, dni: str, cuenta_bancaria: str):
		c = TestUsuarioCliente(nombre, email, dni, cuenta_bancaria, 'a')
		len_antes = len(self.usuarios)
		self.usuarios.append(c)
		assert len(self.usuarios) > len_antes
		
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		assert cliente.get_nombre() == nombre
		assert cliente.get_email() == email
		assert cliente.get_cuenta_bancaria() == cuenta_bancaria
		
	# [HU3] Administrar usuario: Modificación administrador
	def modificar_admin(self, nombre: str, email: str, dni: str):
		admin = [c for c in self.usuarios if c.get_dni() == dni][0]
		assert admin.get_dni() == dni
		
		admin.set_nombre(nombre)
		admin.set_email(email)
		email_empresarial = email.split('@')[0] + '@medauth.com'
		admin.set_email_empresarial(email_empresarial)
		
		assert admin.get_nombre() == nombre
		assert admin.get_email() == email
		assert admin.get_email_empresarial() == email_empresarial
	
	# [HU3] Administrar usuario: Modificación cliente
	def modificar_cliente(self, nombre: str, email: str, dni: str, cuenta_bancaria: str):
		cliente = [c for c in self.usuarios if c.get_dni() == dni][0]
		assert cliente.get_dni() == dni
		
		cliente.set_nombre(nombre)
		cliente.set_email(email)
		cliente.set_cuenta_bancaria(cuenta_bancaria)
		
		assert cliente.get_nombre() == nombre
		assert cliente.get_email() == email
		assert cliente.get_cuenta_bancaria() == cuenta_bancaria
		
	
	# [HU3] Administrar usuario: Eliminar usuario
	def eliminar_usuario(self, dni: str):
		len_antes = len(self.usuarios)
		usuario = [c for c in self.usuarios if c.get_dni() == dni][0]
		self.usuarios.remove(usuario)
		assert len(self.usuarios) < len_antes
		
def test_crear_admin():
	t = TestController()
	t.crear_admin("Carlos", "carlos7ma@gmail.com", "75925767-F")
	
def test_crear_cliente():
	t = TestController()
	t.crear_cliente("Juan", "juan@gmail.com", "77925767-Z", "ES12345678")
	
def test_modificar_admin():
	t = TestController()
	t.modificar_admin("Carlos", "terceto@gmail.com", "75925767-F")

def test_modificar_cliente():
	t = TestController()
	t.modificar_cliente("Juan", "juan@gmail.com", "77925767-Z", "ES11223344")

def test_eliminar_usuario():
	t = TestController()
	t.eliminar_usuario("75925767-F")

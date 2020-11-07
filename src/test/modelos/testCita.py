from .testUsuarioCliente import TestUsuarioCliente
from typing import List
import datetime


class TestCita:
	def __init__(self, id_autorizacion: str, asegurado: TestUsuarioCliente, id_prescripcion: str, fecha: datetime, hora: datetime, facultativo_realizador: str, consulta: str):
		self.__id_autorizacion = id_autorizacion
		self.__asegurado = asegurado
		self.__id_prescripcion = id_prescripcion
		self.__fecha = fecha
		self.__hora = hora
		self.__facultativo_realizador = facultativo_realizador
		self.__consulta = consulta

	def get_id_autorizacion(self):
		return self.__id_autorizacion

	def get_asegurado(self):
		return self.__asegurado

	def get_id_prescripcion(self):
		return self.__id_prescripcion

	def get_fecha(self):
		return self.__fecha

	def set_fecha(self, fecha):
		self.__fecha = fecha

	def get_hora(self):
		return self.__hora

	def set_hora(self, hora):
		self.__hora = hora

	def get_facultativo_realizador(self):
		return self.__facultativo_realizador

	def set_facultativo_realizador(self, facultativo_realizador):
		self.facultativo_realizador = facultativo_realizador

	def get_consulta(self):
		return self.__consulta

	def set_consulta(self, consulta):
		self.__consulta = consulta

	def __eq__(self, otra):
		assert self.__id_autorizacion == otra.get_id_autorizacion()
		assert self.__asegurado == otra.get_asegurado()
		assert self.__id_prescripcion == otra.get_id_prescripcion()
		assert self.__fecha == otra.get_fecha()
		assert self.__hora == otra.get_hora()
		assert self.__facultativo_realizador == otra.get_facultativo_realizador()
		assert self.__consulta == otra.get_consulta()

		return ((self.__id_autorizacion == otra.get_id_autorizacion()) and (self.__asegurado == otra.get_asegurado()) and (self.__id_prescripcion == otra.get_id_prescripcion()) and (self.__fecha == otra.get_fecha()) and (self.__hora == otra.get_hora()) and (self.__facultativo_realizador == otra.get_facultativo_realizador()) and (self.__consulta == otra.get_consulta()))

def test_compare_autorizacion():
	u = TestUsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	fecha = datetime.datetime(2020, 5, 17)
	hora = datetime.time(3, 45, 12)
	
	t1 = TestCita("AU-77925767-1", u, "PR-77925767-1", fecha, hora, "D. Fernando", "Centro médico capital, Sala 2")
	t2 = TestCita("AU-77925767-1", u, "PR-77925767-1", fecha, hora, "D. Fernando", "Centro médico capital, Sala 2")
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test
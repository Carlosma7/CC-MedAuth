from .testUsuarioCliente import TestUsuarioCliente
from typing import List
import datetime


class TestAutorizacion:
	def __init__(self, id_autorizacion: str, asegurado: TestUsuarioCliente, id_prescripcion: str, id_poliza: str, estado: str, motivo_rechazo: str, fecha_realizacion: datetime, servicios_aceptados: List[str], facultativo_realizador: str, consulta: str):
		self.__id_autorizacion = id_autorizacion
		self.__asegurado = asegurado
		self.__id_prescripcion = id_prescripcion
		self.__id_poliza = id_poliza
		self.__estado = estado
		self.__motivo_rechazo = motivo_rechazo
		self.__fecha_realizacion = fecha_realizacion
		self.__servicios_aceptados = servicios_aceptados
		self.__facultativo_realizador = facultativo_realizador
		self.__consulta = consulta

	def get_id_autorizacion(self):
		return self.__id_autorizacion

	def get_asegurado(self):
		return self.__asegurado

	def get_id_prescripcion(self):
		return self.__id_prescripcion

	def get_id_poliza(self):
		return self.__id_poliza

	def get_estado(self):
		return self.__estado

	def set_estado(self, estado):
		self.__estado == estado

	def get_motivo_rechazo(self):
		return self.__motivo_rechazo

	def set_motivo_rechazo(self, motivo_rechazo):
		self.__motivo_rechazo = motivo_rechazo

	def get_fecha_realizacion(self):
		return self.__fecha_realizacion

	def set_fecha_realizacion(self, fecha_realizacion):
		self.__fecha_realizacion = fecha_realizacion

	def get_servicios_aceptados(self):
		return self.__servicios_aceptados

	def set_servicios_aceptados(self, servicios_aceptados):
		self.__servicios_aceptados = servicios_aceptados

	def get_facultativo_realizador(self):
		return self.__facultativo_realizador

	def set_facultativo_realizador(self, facultativo_realizador):
		self.__facultativo_realizador = facultativo_realizador

	def get_consulta(self):
		return self.__consulta

	def set_consulta(self, consulta):
		self.__consulta = consulta

	def __eq__(self, otra):
		assert self.__id_autorizacion == otra.get_id_autorizacion()
		assert self.__asegurado == otra.get_asegurado()
		assert self.__id_prescripcion == otra.get_id_prescripcion()
		assert self.__id_poliza == otra.get_id_poliza()
		assert self.__estado == otra.get_estado()
		assert self.__motivo_rechazo == otra.get_motivo_rechazo()
		assert self.__fecha_realizacion == otra.get_fecha_realizacion()
		assert self.__servicios_aceptados == otra.get_servicios_aceptados()
		assert self.__facultativo_realizador == otra.get_facultativo_realizador()
		assert self.__consulta == otra.get_consulta()

		return ((self.__id_autorizacion == otra.get_id_autorizacion()) and (self.__asegurado == otra.get_asegurado()) and (self.__id_prescripcion == otra.get_id_prescripcion()) and (self.__id_poliza == otra.get_id_poliza()) and (self.__estado == otra.get_estado()) and (self.__motivo_rechazo == otra.get_motivo_rechazo()) and (self.__fecha_realizacion == otra.get_fecha_realizacion()) and (self.__servicios_aceptados == otra.get_servicios_aceptados()) and (self.__facultativo_realizador == otra.get_facultativo_realizador()) and (self.__consulta == otra.get_consulta()))
		
def test_compare_autorizacion():
	u = TestUsuarioCliente("Carlos", "carlos7ma@gmail.com", "75925767-F", "ES12345678", "12345678")
	fecha = datetime.datetime(2020, 5, 17)
	
	t1 = TestAutorizacion("AU-12345678", u, "MA-75925767-1", "PR-12345678", "Aceptada", "", fecha, ["Radiografía", "Ortopedia"], "D. Manuel", "Centro médico capital, Sala 2")
	t2 = TestAutorizacion("AU-12345678", u, "MA-75925767-1", "PR-12345678", "Aceptada", "", fecha, ["Radiografía", "Ortopedia"], "D. Manuel", "Centro médico capital, Sala 2")
	
	assert t1 == t1 # Pasa test
	assert t1 == t2 # Pasa test
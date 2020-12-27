from usuarioCliente import UsuarioCliente
from typing import List
import datetime
import json

# Clase de cita médica
class Cita:
	def __init__(self, id_autorizacion: str, asegurado: UsuarioCliente, id_prescripcion: str, fecha: datetime, hora: datetime, facultativo_realizador: str, consulta: str):
		self.__id_autorizacion = id_autorizacion
		self.__asegurado = asegurado
		self.__id_prescripcion = id_prescripcion
		self.__fecha = fecha
		self.__hora = hora
		self.__facultativo_realizador = facultativo_realizador
		self.__consulta = consulta

	# Métodos get/set
	def get_id_autorizacion(self):
		return self.__id_autorizacion

	def get_asegurado(self):
		return self.__asegurado

	def get_id_prescripcion(self):
		return self.__id_prescripcion

	def get_fecha(self):
		return self.__fecha

	def set_fecha(self, fecha: datetime):
		self.__fecha = fecha

	def get_hora(self):
		return self.__hora

	def set_hora(self, hora: datetime):
		self.__hora = hora

	def get_facultativo_realizador(self):
		return self.__facultativo_realizador

	def set_facultativo_realizador(self, facultativo_realizador: str):
		self.facultativo_realizador = facultativo_realizador

	def get_consulta(self):
		return self.__consulta

	def set_consulta(self, consulta: str):
		self.__consulta = consulta

	# Override método equal
	def __eq__(self, otra):
		return ((self.__id_autorizacion == otra.get_id_autorizacion()) and (self.__asegurado == otra.get_asegurado()) and (self.__id_prescripcion == otra.get_id_prescripcion()) and (self.__fecha == otra.get_fecha()) and (self.__hora == otra.get_hora()) and (self.__facultativo_realizador == otra.get_facultativo_realizador()) and (self.__consulta == otra.get_consulta()))

	# Método para transformar objeto en un dict
	def to_dict(self):
		return {'id_autorizacion': self.__id_autorizacion, 'asegurado': self.__asegurado.to_dict(), 'id_prescripcion': self.__id_prescripcion, 'fecha': self.__fecha.strftime('%m/%d/%Y'), 'hora': self.__hora.strftime('%H:%M'), 'facultativo_realizador': self.__facultativo_realizador, 'consulta': self.__consulta}

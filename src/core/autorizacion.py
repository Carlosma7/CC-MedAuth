from usuarioCliente import UsuarioCliente
from especialidad import Especialidad
from typing import List
import datetime

# Clase de autorización médica
class Autorizacion:
	def __init__(self, id_autorizacion: str, asegurado: UsuarioCliente, id_prescripcion: str, id_poliza: str, aceptada: bool, motivo_rechazo: str, fecha_realizacion: datetime, especialidad: Especialidad, servicios_aceptados: List[str], facultativo_realizador: str, consulta: str):
		self.__id_autorizacion = id_autorizacion
		self.__asegurado = asegurado
		self.__id_prescripcion = id_prescripcion
		self.__id_poliza = id_poliza
		self.__aceptada = aceptada
		self.__motivo_rechazo = motivo_rechazo
		self.__fecha_realizacion = fecha_realizacion
		self.__especialidad = especialidad
		self.__servicios_aceptados = servicios_aceptados
		self.__facultativo_realizador = facultativo_realizador
		self.__consulta = consulta

	# Métodos get/set
	def get_id_autorizacion(self):
		return self.__id_autorizacion
	
	def set_id_autorizacion(self, id_autorizacion: str):
		self.__id_autorizacion = id_autorizacion

	def get_asegurado(self):
		return self.__asegurado

	def get_id_prescripcion(self):
		return self.__id_prescripcion

	def get_id_poliza(self):
		return self.__id_poliza

	def get_aceptada(self):
		return self.__aceptada

	def set_aceptada(self, aceptada: bool):
		self.__aceptada = aceptada

	def get_motivo_rechazo(self):
		return self.__motivo_rechazo

	def set_motivo_rechazo(self, motivo_rechazo: str):
		self.__motivo_rechazo = motivo_rechazo

	def get_fecha_realizacion(self):
		return self.__fecha_realizacion

	def set_fecha_realizacion(self, fecha_realizacion: datetime):
		self.__fecha_realizacion = fecha_realizacion

	def get_especialidad(self):
		return self.__especialidad

	def set_especialidad(self, especialidad: Especialidad):
		self.__especialidad = especialidad

	def get_servicios_aceptados(self):
		return self.__servicios_aceptados

	def set_servicios_aceptados(self, servicios_aceptados: List[str]):
		self.__servicios_aceptados = servicios_aceptados

	def get_facultativo_realizador(self):
		return self.__facultativo_realizador

	def set_facultativo_realizador(self, facultativo_realizador: str):
		self.__facultativo_realizador = facultativo_realizador

	def get_consulta(self):
		return self.__consulta

	def set_consulta(self, consulta: str):
		self.__consulta = consulta

	# Override método equal
	def __eq__(self, otra):
		return ((self.__id_autorizacion == otra.get_id_autorizacion()) and (self.__asegurado == otra.get_asegurado()) and (self.__id_prescripcion == otra.get_id_prescripcion()) and (self.__id_poliza == otra.get_id_poliza()) and (self.__aceptada == otra.get_aceptada()) and (self.__motivo_rechazo == otra.get_motivo_rechazo()) and (self.__fecha_realizacion == otra.get_fecha_realizacion()) and (self.__especialidad == otra.get_especialidad()) and (self.__servicios_aceptados == otra.get_servicios_aceptados()) and (self.__facultativo_realizador == otra.get_facultativo_realizador()) and (self.__consulta == otra.get_consulta()))

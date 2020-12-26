from usuarioCliente import UsuarioCliente
from especialidad import Especialidad
from typing import List
import datetime
import json

# Clase de prescripción médica
class Prescripcion:
	def __init__(self, id_prescripcion: str, asegurado: UsuarioCliente, id_poliza: str, fecha_realizacion: datetime, especialidad: Especialidad, facultativo_prescriptor: str, facultativo_realizador: str, servicios_solicitados: List[str], consulta: str):
		self.__id_prescripcion = id_prescripcion
		self.__asegurado = asegurado
		self.__id_poliza = id_poliza
		self.__fecha_realizacion = fecha_realizacion
		self.__especialidad = especialidad
		self.__facultativo_prescriptor = facultativo_prescriptor
		self.__facultativo_realizador = facultativo_realizador
		self.__servicios_solicitados = servicios_solicitados[:]
		self.__consulta = consulta

	# Métodos get/set
	def get_id_prescripcion(self):
		return self.__id_prescripcion

	def set_id_prescripcion(self, id_prescripcion):
		self.__id_prescripcion = id_prescripcion

	def get_asegurado(self):
		return self.__asegurado

	def get_id_poliza(self):
		return self.__id_poliza

	def get_fecha_realizacion(self):
		return self.__fecha_realizacion

	def get_especialidad(self):
		return self.__especialidad

	def get_facultativo_prescriptor(self):
		return self.__facultativo_prescriptor

	def get_facultativo_realizador(self):
		return self.__facultativo_realizador

	def get_servicios_solicitados(self):
		return self.__servicios_solicitados

	def get_consulta(self):
		return self.__consulta

	# Override método equal
	def __eq__(self, otra):
		return ((self.__id_prescripcion == otra.get_id_prescripcion()) and (self.__asegurado == otra.get_asegurado()) and (self.__id_poliza == otra.get_id_poliza()) and (self.__fecha_realizacion == otra.get_fecha_realizacion()) and (self.__especialidad == otra.get_especialidad()) and (self.__facultativo_prescriptor == otra.get_facultativo_prescriptor()) and (self.__facultativo_realizador == otra.get_facultativo_realizador()) and (self.__servicios_solicitados == otra.get_servicios_solicitados()) and (self.__consulta == otra.get_consulta()))

    # Método para transformar objeto en un dict
	def to_dict(self):
		return {'id_prescripcion': self.__id_prescripcion, 'asegurado': self.__asegurado.to_dict(), 'id_poliza': self.__id_poliza, 'fecha_realizacion': self.__fecha_realizacion.strftime('%m/%d/%Y'), 'especialidad': json.dumps(self.__especialidad), 'facultativo_prescriptor': self.__facultativo_prescriptor, 'facultativo_realizador': self.__facultativo_realizador, 'servicios_solicitados': self.__servicios_solicitados, 'consulta': self.__consulta}

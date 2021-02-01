from usuarioCliente import UsuarioCliente
from tipoPoliza import TipoPoliza
from moduloExtra import ModuloExtra
from typing import List
import datetime
import json


# Clase de póliza de asegurado
class Poliza:

    def __init__(self, usuario: UsuarioCliente, id_poliza: str, periodo_carencia: datetime, tipo: TipoPoliza,
    			copagos: float, mensualidad: str, servicios_excluidos: List[str], modulos_extra: List[ModuloExtra], activa: bool):
        self.__titular = usuario
        self.__id_poliza = id_poliza
        self.__periodo_carencia = periodo_carencia
        self.__tipo = tipo
        self.__copagos = copagos
        self.__mensualidad = mensualidad
        self.__servicios_excluidos = servicios_excluidos[:]
        self.__modulos_extra = modulos_extra[:]
        self.__activa = activa
    
    @classmethod
    def from_dict(cls, data: dict):
        # Obtener usuario
        usuario = UsuarioCliente.from_dict(data.get('titular'))
        # Obtener periodo carencia
        periodo_carencia = datetime.datetime.strptime(data.get('periodo_carencia'), '%m/%d/%Y')
        # Obtener tipo de póliza
        tipo = TipoPoliza(json.loads(data.get('tipo')))

        p = cls(usuario, data.get('id_poliza'), periodo_carencia, tipo, data.get('copagos'), data.get('mensualidad'), data.get('servicios_excluidos'), data.get('modulos_extra'), data.get('activa'))
        return p

    # Métodos get/set
    def get_titular(self):
    	return self.__titular

    def get_id_poliza(self):
    	return self.__id_poliza

    def set_id_poliza(self, id_poliza: str):
    	self.__id_poliza = id_poliza

    def get_periodo_carencia(self):
    	return self.__periodo_carencia

    def set_periodo_carencia(self, periodo_carencia: datetime):
    	self.__periodo_carencia == periodo_carencia

    def get_tipo(self):
    	return self.__tipo

    def set_tipo(self, tipo: TipoPoliza):
    	self.__tipo = tipo

    def get_copagos(self):
    	return self.__copagos

    def set_copagos(self, copagos: float):
    	self.__copagos = copagos

    def get_mensualidad(self):
    	return self.__mensualidad

    def set_mensualidad(self, mensualidad: float):
    	self.__mensualidad = mensualidad

    def get_servicios_excluidos(self):
    	return self.__servicios_excluidos

    def set_servicios_excluidos(self, servicios_excluidos: List[str]):
    	self.__servicios_excluidos = servicios_excluidos[:]

    def get_modulos_extra(self):
    	return self.__modulos_extra

    def set_modulos_extra(self, modulos_extra: List[ModuloExtra]):
    	self.__modulos_extra = modulos_extra[:]

    def get_activa(self):
    	return self.__activa

    def set_activa(self, activa: bool):
    	self.__activa = activa

    # Override método equal
    def __eq__(self, otra):
    	return (self.__titular == otra.get_titular()) and (self.__id_poliza == otra.get_id_poliza()) and (self.__periodo_carencia == otra.get_periodo_carencia()) and (self.__tipo == otra.get_tipo()) and (self.__copagos == otra.get_copagos()) and (self.__mensualidad == otra.get_mensualidad()) and (self.__servicios_excluidos == otra.get_servicios_excluidos() and (self.__modulos_extra == otra.get_modulos_extra()) and (self.__activa == otra.get_activa()))

    # Método para transformar objeto en un dict
    def to_dict(self):
        return {'titular': self.__titular.to_dict(), 'id_poliza': self.__id_poliza, 'periodo_carencia': self.__periodo_carencia.strftime('%m/%d/%Y'), 'tipo': json.dumps(self.__tipo), 'copagos': self.__copagos, 'mensualidad': self.__mensualidad, 'servicios_excluidos': self.__servicios_excluidos, 'modulos_extra': self.__modulos_extra, 'activa': self.__activa}

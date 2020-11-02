from .usuario import Usuario
from typing import List
import datetime


class Autorizacion:

    def __init__(self):
        self.id_autorizacion: str
        self.asegurado: Usuario
        self.id_prescripcion: str
        self.id_poliza: str
        self.estado: str
        self.motivo_rechazo: str
        self.fecha_realizacion: str
        self.servicios_aceptados: List[str]
        self.facultativo_realizador: str
        self.consulta: str

from .usuario import Usuario
from typing import List
import datetime


class Cita:

    def __init__(self):
        self.asegurado: Usuario
        self.id_autorizacion: str
        self.id_prescripcion: str
        self.fecha: datetime
        self.hora: datetime
        self.facultativo_realizador: str
        self.consulta: str

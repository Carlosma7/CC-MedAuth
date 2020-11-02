from models.usuario.usuario import Usuario
from typing import List
import datetime


class Prescripcion:

    def __init__(self):
        self.id_prescripcion: str
        self.asegurado: Usuario
        self.id_poliza: str
        self.fecha_realizacion: datetime
        self.especialidad: str
        self.facultativo_prescriptor: str
        self.facultativo_realizador: str
        self.servicios_solicitados: List[str]
        self.consulta: str

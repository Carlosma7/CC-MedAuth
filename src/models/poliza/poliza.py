from models.usuario.usuario import Usuario
from typing import List
import datetime


class Poliza:

    def __init__(self):
        self.titular: Usuario
        self.periodo_carencia: datetime
        self.tipo: str
        self.copagos: float
        self.mensualidad: float
        self.servicios_excluidos: List[str]

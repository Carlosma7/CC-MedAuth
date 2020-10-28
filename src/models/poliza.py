from typing import List
import datetime


class Poliza:

    def __init__(self):
        self.titular: str
        self.periodoCarencia: datetime
        self.tipo: str
        self.copagos: float
        self.mensualidad: float
        self.serviciosExcluidos: List[str]



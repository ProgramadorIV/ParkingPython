from enum import Enum

class EstadoPlaza(Enum):
    LIBRE = 'libre'
    OCUPADA = 'ocupada'
    ABONOOCUPADA = 'abono ocupada'
    ABONOLIBRE = 'abono libre'
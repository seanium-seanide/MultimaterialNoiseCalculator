from dataclasses import dataclass
from numpy import float64, int64

@dataclass
class Material:
    name: str
    a: int64
    alpha: float64
    beta: float64
    kappa: int64
    C: float64
    n: float64
    Y: float64
    prat: float64
    phiM: float64

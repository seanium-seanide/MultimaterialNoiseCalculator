import dataclasses
from numpy import float64

@dataclasses.dataclass
class Material:
    name: str = ""          # Description
    a: float64 = 0.0        # Absorption per length
    alpha: float64 = 0.0    # Thermal expansion coefficient
    beta: float64 = 0.0     # Derivative of refractive index w.r.t temperature
    kappa: float64 = 0.0    # Thermal conductivity
    C: float64 = 0.0        # Heat capacity per volume
    n: float64 = 0.0        # Refractive index
    Y: float64 = 0.0        # Young's modulus
    prat: float64 = 0.0     # Poisson's rratio
    phiM: float64 = 0.0     # Mechanical loss

    """
    def __post_init__(self):
        for field in dataclasses.fields(self):
            if not isinstance(field.default, dataclasses._MISSING_TYPE) \
                    and getattr(self, field.name) is None:
                setattr(self, field.name, field.default)
    """

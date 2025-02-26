from dataclasses import dataclass
from numpy import float64

@dataclass
class Interferometer:
    w: float64 = 0  # Beam width
    wl: float64 = 0 # Wavelength / nm
    T: float64 = 0  # Temperature / K

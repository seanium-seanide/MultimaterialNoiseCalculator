import numpy as np

def getCoatAbsorption(wl, dOpt, aLayer, nLayer, rbar, r):
    '''
    Inputs
    ------

    wl: wavelength
    dOpt: optical thickness
    aLayer: absorption per unit length in each layer
    nLayer: refractive indices of layers (input layer to output layer)
    rbar: amplitude reflectivity of coating from given layer down
    r: amplitude interface of given interface

    Outputs
    -------

    absCoat: coating total absorption
    absLayer: absorption contribution from each layer
    rho: power ratio in each layer
    powerLayer: Power in each layer

    References
    ----------

    See getCoatRefl
    '''

    # Power in each layer
    a = 1 - r[:-1]**2
    b = (1 + r[:-1] * rbar)**2
    powerLayer = np.cumprod(np.abs(a/b))

    # One-way phase in each layer
    phi = 2 * np.pi * dOpt

    # Average squared electric field in each layer
    a = 1 + np.abs(rbar)**2
    b = 2 * (np.sin(phi) / phi) * np.real(rbar * np.exp(1j * phi))
    rho = a + b

    # TODO: Dimensionally incorrect!
    # Geometrical thickness of each layer
    dGeo = wl * dOpt / nLayer

    # Power weighing factor for each layer
    absLayer = aLayer * rho * powerLayer * dGeo

    # Total coating absorption
    absCoat = np.sum(absLayer)

    return absCoat, absLayer, powerLayer, rho

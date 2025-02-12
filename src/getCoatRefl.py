import numpy as np

def getCoatRefl(nIn, nOut, nLayer, dOpt):
    """
    Inputs
    ------

    nIn: Input medium refractive index
    nOut: Output medium refractive index
    nLayer: Refractive index of each layer, ordered input to output (N x 1)
    dOpt: Optical thickness / wl, for each layer


    Outputs
    -------

    rCoat: Amplitude reflectivity of coating stack
    dcdp: d reflection phase / d round-trip layer phase
    rbar: amplitude reflectivity of coating from each layer downwards
    r: amplitude reflectivity of each interface

    References
    ----------

    * GWINC: getCoatRefl and getCoatTOPhase
    * T080101
    """
    # Refractive indices
    nAll = np.zeros(np.size(nLayer) + 2, dtype=np.float64)
    nAll[0] = nIn
    nAll[1:np.size(nLayer) + 1] = nLayer
    nAll[np.size(dOpt) + 1] = nOut

    # Reflectance at each interface
    a = nAll[:-1] - nAll[1:]
    b = nAll[:-1] + nAll[1:]
    r = a / b

    # Combine reflectances
    rbar = np.zeros(np.size(r), dtype=np.complex128)
    ephi = np.zeros(np.size(r), dtype=np.complex128)
    ephi[-1] = np.exp(-4j * np.pi * dOpt[-1]);
    rbar[-1] = ephi[-1] * r[-1];
    for i in range(len(dOpt) - 1, -1, -1):
        if i > 0:
            ephi[i] = np.exp(-4j * np.pi * dOpt[i-1])
        else:
            ephi[i] = 1

        a = r[i] + rbar[i + 1]
        b = 1 + r[i] * rbar[i + 1]
        rbar[i] = ephi[i] * a / b

    # Reflectance derivatives
    dr_dphi = np.zeros(np.size(dOpt), dtype=np.complex128)
    for i in range(len(dOpt) - 1, -1, -1):
        dr_dphi[i] = -1j * rbar[i + 1]
        for j in range(i, -1, -1):
            a = 1 - r[j] ** 2
            b = (1 + r[j] * rbar[j + 1]) ** 2
            dr_dphi[i] = dr_dphi[i] * ephi[j] * a / b

    # Shift rbar index
    rCoat = rbar[0]
    rbar = rbar[1:]

    # Phase derivatives
    dcdp = np.imag(dr_dphi / rCoat)

    return rCoat, dcdp, rbar, r

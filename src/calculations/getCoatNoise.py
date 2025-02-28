import numpy as np

def getCoatNoise(f, wl, wBeam, T, materialParams, materialSub, materialLayer
        , dOpt, dcdp):
    """
    Inputs
    ------
    f: Frequency
    wl: Wavelength
    wBeam: Beam width
    T: Temperature
    materialParams: Material parameters (Python list of class Material)
    materialSub: Substrate Material (string)
    materialLayer:
    dOpt:
    dcdp:

    Outputs
    -------
    SbrZ: Coating brownian noise
    StoZ: Thermo-optic noise
    SteZ: Thermo-elastic noise
    StrZ: Thermo-refractive noise
    brLayer: Coating thermal noise for each layer
    """

    # Reciprocal thermodynamic beta
    kT = 1.3807e-23 * T

    # Angular Frequency
    omega = 2 * np.pi * f

    # Substrate thermal, optical, and mechanical properties
    alphaSub = materialParams[materialSub].alpha
    cSub = materialParams[materialSub].C
    kappaSub = materialParams[materialSub].kappa
    ySub = materialParams[materialSub].Y
    pratSub = materialParams[materialSub].prat

    # Material property vectors
    nN = np.zeros(np.size(dOpt), np.float64)
    aN = np.zeros(np.size(dOpt), np.float64)
    alphaN = np.zeros(np.size(dOpt), np.float64)
    betaN = np.zeros(np.size(dOpt), np.float64)
    kappaN = np.zeros(np.size(dOpt), np.float64)
    cN = np.zeros(np.size(dOpt), np.float64)
    yN = np.zeros(np.size(dOpt), np.float64)
    pratN = np.zeros(np.size(dOpt), np.float64)
    phiN = np.zeros(np.size(dOpt), np.float64)
    for i in range(np.size(materialLayer)):
        nN[i] = materialParams[materialLayer[i]].n
        aN[i] = materialParams[materialLayer[i]].a
        alphaN[i] = materialParams[materialLayer[i]].alpha
        betaN[i] = materialParams[materialLayer[i]].beta
        kappaN[i] = materialParams[materialLayer[i]].kappa
        cN[i] = materialParams[materialLayer[i]].C
        yN[i] = materialParams[materialLayer[i]].Y
        pratN[i] = materialParams[materialLayer[i]].prat
        phiN[i] = materialParams[materialLayer[i]].phiM

    # Geometrical thicknesses
    dGeo = wl * dOpt / nN
    dCoat = np.sum(dGeo)

    ##################
    # Brownian Noise #
    ##################

    # Layer contributions
    a = (1 + nN * dcdp / 2)**2 * (ySub / yN)
    b = (1 - pratSub - 2 * pratSub**2)**2 * yN
    c = ((1 + pratN)**2 * (1 - 2 * pratN) * ySub)
    d = (1 - pratN)
    e = ((1 - pratN - 2 * pratN**2))
    f = ((1 - pratSub - 2 * pratSub**2))
    brLayer = (a + b / c) / d * e / f

    # Sum contributions
    a = 4 * kT / (np.pi * wBeam**2 * omega)
    b = 1 - pratSub - 2 * pratSub ** 2
    SbrZ = a * sum(dGeo * brLayer * phiN * b / ySub);

    ######################
    # Thermo-optic Noise #
    ######################

    # Substrate alpha
    alphaBarSub = 2 * (1 + pratSub) * alphaSub

    # Layer contributions

    alphaBar = (dGeo / dCoat) * ((1 + pratSub) / (1 - pratN)) * \
    ((1 + pratN) / (1 + pratSub) + (1 - 2 * pratSub) * yN / ySub) * alphaN

    betaBar = (-dcdp) * dOpt * \
    (betaN / nN + alphaN * (1 + pratN) / (1 - pratN))

    #
    # Warning: Extra factor of T???
    #

    # Thermo-elastic
    SteZ = (4 * kT * T / (np.pi * wBeam**2 * np.sqrt(2 * kappaSub * cSub * omega))) * \
    (sum(alphaBar * dCoat) - alphaBarSub * sum(dGeo * cN) / cSub)**2

    # Thermo-refractive
    StrZ = (4 * kT * T / (np.pi * wBeam**2 * np.sqrt(2 * kappaSub * cSub * omega))) * \
    sum(betaBar * wl)**2;

    # Total thermo-optic
    StoZ = (4 * kT * T / (np.pi * wBeam**2 * np.sqrt(2 * kappaSub * cSub * omega))) * \
    (sum(alphaBar * dCoat) - sum(betaBar * wl) - \
      alphaBarSub * sum(dGeo * cN) / cSub )**2

    # Return
    return SbrZ, StoZ, SteZ, StrZ, brLayer

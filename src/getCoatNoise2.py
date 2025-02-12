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
    SbrZ
    StoZ
    SteZ
    StrZ
    BrLayer
    """

    # Reciprocal thermodynamic beta
    kT = 1.3806e-23 * T

    # Angular Frequency
    omega = 2 * pi * f

    # Substrate thermal, optical, and mechanical properties
    alphaSub = materialParams[materialSub].alpha
    cSub = materialParams[materialSub].C
    kappaSub = materialParams[materialSub].kappa
    ySub = materialParams[materialSub].Y
    pratSub = materialParams[materialSub].prat

    # Material property vectors
    nN = np.zeros(np.size(dOpt), np.float64)
    aN = np.zeros(np.size(dOpt), np.int32)
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
    dGeo = lambda * dOpt / nN
    dCoat = np.sum(dGeo)

    ##################
    # Brownian Noise #
    ##################

    # Layer contributions
    a1 = (1 + nN * dcdp / 2) ** 2 * (ySub / yN)
    a2 = (1 - pratSub - 2 * pratSub.^2)**2 * yN
    a3 = (1 + pratN) ** 2 * (1 - 2 * pratN) * ySub
    a = (1 + nN * dcdp / 2) ** 2 * (ySub / yN) +  a2 / a3
    b = 1 - pratN
    c = 1 - pratN - 2 * pratN.^2
    d = 1 - pratSub - 2 * pratSub.^2
    brLayer = a / b * c / d

    # Sum contributions
    a = 4 * kBT / (pi * wBeam^2 * w)
    b = 1 - pratSub - 2 * pratSub ** 2
    SbrZ = a * sum(dGeo * brLayer * phiN * b / ySub);

    ######################
    # Thermo-optic Noise #
    ######################

    # Substrate alpha
    alphaBarSub

    # Layer contributions

    # Thermo-elastic

    # Thermo-refractive

    # Total thermo-optic

    # Return
    SbrZ = 0
    StoZ = 0
    SteZ = 0
    StrZ = 0
    BrLayer = 0
    return SbrZ, StoZ, SteZ, StrZ, BrLayer

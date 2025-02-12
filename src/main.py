import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["text.usetex"] = True

from Material import Material
from getCoatAbsorption import getCoatAbsorption
from getCoatRefl import getCoatRefl
from getCoatNoise import getCoatNoise

########
# Data #
########

# Interferometer params
wBeam = 0.062
wl = 1064e-9
Temp = 290

# Plotting frequencies
f = np.logspace(0, 2, 100)

# Material index
#   MaterialLayer[0]: Cap layeer
#   MaterialLayer[N-1]: Substrate
num21 = 19
num31 = 0
numBilayers = num21 + num31
numLayers = 2 * numBilayers
materialLayer = np.empty(numLayers, dtype=np.int32)
materialLayer[:2*num21] = np.tile([0, 1], num21) 
materialLayer[2*num21:] = np.tile([0, 2], num31)

# Optical thickness of each layer
dOpt = np.full(numLayers, 0.25)
dOpt[0] = 0.5

# Material index of substrate material
materialSub = 2 # 3 in Matlab

# Materials
silica = Material("SiO2", 2, 1e-6, 1e-6, 1, 1e6, 1.45, 72e9, 0.17, 0.5e-4)
tiSilica = Material("Ti:SiO2", 0, 1e-6, 1e-6, 1, 1e6, 2.07, 140e9, 0.28, 3.3e-4)
silicaSubstrate = Material("SiO2-substrate", 0, 1e-6, 1e-6, 1, 1e6, 1.45, 73.2e9, 0.17, 1e-9)
materialParams = [silica, tiSilica, silicaSubstrate]

# Substrate
nSub = materialParams[materialSub].n
ySub = materialParams[materialSub].Y
pratSub = materialParams[materialSub].prat

# Material property vectors
nLayer = np.zeros(numLayers)
aLayer = np.zeros(numLayers, dtype=np.int32)
for i in range(numLayers):
    nLayer[i] = materialParams[materialLayer[i]].n
    aLayer[i] = materialParams[materialLayer[i]].a

# Get reflectance
rCoat, dcdp, rbar, r = getCoatRefl(1, nSub, nLayer, dOpt)

# Get absorption
absCoat, absLayer, powerLayer, rho = getCoatAbsorption(wl, dOpt, aLayer, nLayer, rbar, r);

# Get brownian and thermo-optic noise
SbrZ, StoZ, SteZ, StrZ, brLayer = getCoatNoise(
    f, wl, wBeam, Temp, materialParams, materialSub, materialLayer, dOpt, dcdp
)

#########
# Plots #
#########

# Absorption

fig1, ax1 = plt.subplots()
ax1.set_yscale("log")

ax1.scatter(np.arange(1, len(rho) + 1), rho, marker='o', label=r"$\rho_j$")
ax1.scatter(np.arange(1, len(rho) + 1), powerLayer, marker='o', label=r"$P_j/P_0$")
ax1.scatter(np.arange(1, len(rho) + 1), rho * powerLayer, marker='o', label=r"$\bar{\rho}_j$")

ax1.legend(loc="upper right")

ax1.set_title("Absorption Values")
ax1.set_xlabel("Layer Number")
ax1.set_xlim([0, 40])
ax1.set_ylim([1e-6, 1e1])
ax1.grid(axis='x')
ax1.grid(axis='y', linestyle='--')

# Noise weights for each layer

fig2, ax2 = plt.subplots()

ax2.scatter(np.arange(1, len(rho) + 1), -dcdp, marker='o'
        , label=r"$-\partial\phi_c/\partial\phi_j$")
ax2.scatter(np.arange(1, len(rho) + 1), brLayer, marker='o'
        , label=r"$b_j$")

ax2.legend(loc="upper right")

ax2.set_title("Noise Weights for Each Layer")
ax2.set_xlabel("Layer Number")
ax2.set_xlim([0, 40])
ax2.set_ylim([0, 2.5])
ax2.grid(axis='x')
ax2.grid(axis='y', linestyle='--')

# Noise plots

fig3, ax3 = plt.subplots()
ax3.set_xscale("log")
ax3.set_yscale("log")

ax3.plot(f, np.sqrt(SbrZ), "r", label="Brownian Noise")
ax3.plot(f, np.sqrt(StoZ), "b", label="Thermo-optic Noise")
ax3.plot(f, np.sqrt(SteZ), "-.", label="TE Component")
ax3.plot(f, np.sqrt(StrZ), "-.", label="TR Component")

ax3.legend(loc="upper right")

ax3.set_title("Thermal Noise")
ax3.set_xlabel("frequency [Hz]")
ax3.set_ylabel(r"thermal noise [$\textrm{m}/\sqrt{\textrm{Hz}}$]")
ax3.set_xlim([1e0, 1e2])
ax3.set_ylim([1e-22, 1e-19])

# Display plots
plt.show()

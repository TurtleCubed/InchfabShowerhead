"""
This script compares the throughput coming out of each opening by assuming some upstream pressure
"""

import Throughput
import numpy as np
from scipy import optimize
import matplotlib
import matplotlib.pyplot as plt

DT = 0.125
Vars = [78.1, 39, 55, 79, 10]

# general data
temp = 298  # Kelvin
r_0 = 8.314  # in MKS

# pipe_data
# Cross-sectional shape, cross-sectional dimensions, duct length, corners, roughness
# Holes 1 and 6
shapeO16 = "cylinder"
diameterO16 = Vars[1] * 0.001 * 0.0254
lengthO16 = Vars[0] * 0.001 * 0.0254
n_cO16 = 0
# Holes 2 and 5
shapeO25 = "cylinder"
diameterO25 = Vars[2] * 0.001 * 0.0254
lengthO25 = Vars[0] * 0.001 * 0.0254
n_cO25 = 0
# Holes 3 and 4
shapeO34 = "cylinder"
diameterO34 = Vars[3] * 0.001 * 0.0254
lengthO34 = Vars[0] * 0.001 * 0.0254
n_cO34 = 0
# Pipes Ct1 and Ct7
shapeT17 = "cylinder"
diameterT17 = DT * 0.0254
lengthT17 = 0.65 * 0.0254
n_cT17 = 0
# Pipes Ct2-6
shapeT23456 = "cylinder"
diameterT23456 = DT * 0.0254
lengthT23456 = 1.31 * 0.0254
n_cT23456 = 0

# gas_data
# Gamma (heat capacity ratio), molar mass, particle diameter (for mean free path), viscosity
# weighted average 2 parts Nitrogen, 8 parts Argon
gamma = 0.2 * 1.4 + 0.8 * 1.66
molar_mass = 0.2 * 0.02802 + 0.8 * 0.039948  # kg/mol
particle_diameter = (0.2 * 364 + 0.8 * 340) * 10**-12
viscosity = (0.2 * 1.76 + 0.8 * 2.23) * 10**-5  # Pa s

# flow_data
# Upstream pressure, downstream pressure, throughput, Reynolds number
# millitorr * 0.13332237 = pascal
p_chamber = 50 * 0.13332237
throughput = Vars[4] * 101325 / (60 * 10**6)  # convert to Pa m^3/s
throughput = throughput / 6

# def throughput_p(p_upstream, p_downstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
#                  particle_diameter, viscosity, a, b, d, target, ma_n=0.15, single_run=False):
# nodeCN where N refers to the upstream pressure of the referenced pipe

# finding PT1 by going up the shower head
# using O1 as correct
PO1_1 = optimize.newton(Throughput.throughput_p, 50, args=(
    p_chamber, lengthO16, shapeO16, n_cO16, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0,
    diameterO16,
    throughput))
PT1_1 = optimize.newton(Throughput.throughput_p, 100, args=(
    PO1_1, lengthT17, shapeT17, n_cT17, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0, diameterT17,
    throughput * 3))

# using O2 as correct
PO2_2 = optimize.newton(Throughput.throughput_p, 50, args=(
    p_chamber, lengthO25, shapeO25, n_cO25, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0,
    diameterO25,
    throughput))
PO1_2 = optimize.newton(Throughput.throughput_p, 50, args=(
    PO2_2, lengthT23456, shapeT23456, n_cT23456, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0,
    diameterT23456, throughput * 2))
PT1_2 = optimize.newton(Throughput.throughput_p, 100, args=(
    PO1_2, lengthT17, shapeT17, n_cT17, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0, diameterT17,
    throughput * 3))

# using O3 as correct
PO3_3 = optimize.newton(Throughput.throughput_p, 50, args=(
    p_chamber, lengthO34, shapeO34, n_cO34, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0,
    diameterO34, throughput))
PO2_3 = optimize.newton(Throughput.throughput_p, 50, args=(
    PO3_3, lengthT23456, shapeT23456, n_cT23456, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0,
    diameterT23456, throughput))
PO1_3 = optimize.newton(Throughput.throughput_p, 50, args=(
    PO2_3, lengthT23456, shapeT23456, n_cT23456, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0,
    diameterT23456, throughput * 2))
PT1_3 = optimize.newton(Throughput.throughput_p, 100, args=(
    PO1_3, lengthT17, shapeT17, n_cT17, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0, diameterT17,
    throughput * 3))

PT1 = np.mean((PT1_1, PT1_2, PT1_3))
# PT1 = 550 * 0.13332237

# finding the opening throughputs by going back down the shower head
PO1a = optimize.newton(Throughput.throughput_pd, 50, args=(
    PT1, lengthT17, shapeT17, n_cT17, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0, diameterT17,
    throughput * 3))
QO1 = Throughput.throughput_p(PO1a, p_chamber, lengthO16, shapeO16, n_cO16, temp, r_0, gamma, molar_mass,
                              particle_diameter, viscosity, 0, 0, diameterO16, 0)
QT2 = throughput * 3 - QO1
PO2a = optimize.newton(Throughput.throughput_pd, 50, args=(
    PO1a, lengthT23456, shapeT23456, n_cT23456, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0,
    diameterT23456, QT2))
QO2 = Throughput.throughput_p(PO2a, p_chamber, lengthO25, shapeO25, n_cO25, temp, r_0, gamma, molar_mass,
                              particle_diameter, viscosity, 0, 0, diameterO25, 0)
QT3 = QT2 - QO2
QO3 = QT3
# PO3a = optimize.newton(Throughput.throughput_pd, 50, args=(PO2a, lengthT23456, shapeT23456, n_cT23456, temp, r_0,
# gamma, molar_mass, particle_diameter, viscosity, 0, 0, diameterT23456, QT3))

print("PO3 =", PO3_3 / 0.13332237)
print("PO2 =", PO2_3 / 0.13332237)
print("PO1 =", PO1_3 / 0.13332237)
print("PT1 =", PT1_3 / 0.13332237)

QO1 = QO1 / 0.00168875
QO2 = QO2 / 0.00168875
QO3 = QO3 / 0.00168875

print("QO1 =", QO1)
print("QO2 =", QO2)
print("QO3 =", QO3)


x = [1, 2, 3]
y = [QO1, QO2, QO3]
mean = np.mean((QO1, QO2, QO3))
means = [mean, mean, mean]
plt.title("Throughput at Each Opening")
plt.xticks(x, x)
plt.xlabel("Opening Number")
plt.ylabel("Throughput (MKS)")
plt.plot(x, y)
plt.plot(x, means)
label1 = '{:.4}'.format(QO1) + " SCCM"
label2 = '{:.4}'.format(QO2) + " SCCM"
label3 = '{:.4}'.format(QO3) + " SCCM"
plt.text(1, QO1 + mean * 0.1, label1)
plt.text(2, QO2 + mean * 0.1, label2, horizontalalignment="center")
plt.text(3, QO3 + mean * 0.1, label3, horizontalalignment="right")

text = []
text.append("Net throughput: " + '{:.3}'.format(throughput * 6 / 101325 * (60 * 1000000)))
text.append("Aperture length: " + '{:.3}'.format(lengthO16 * 1000 / 0.0254) + " mil")
text.append("Diameter O1: " + '{:.3}'.format(diameterO16 * 1000 / 0.0254) + " mil")
text.append("Diameter O2: " + '{:.3}'.format(diameterO25 * 1000 / 0.0254) + " mil")
text.append("Diameter O3: " + '{:.3}'.format(diameterO34 * 1000 / 0.0254) + " mil")
text.append("Connecting Pipe Diameter: " + '{:.3}'.format(diameterT23456 * 1000 / 0.0254) + " mil")
string = ""
string1 = '{:.3}'.format(lengthO16 * 1000 / 0.0254) + "\t" + \
          '{:.3}'.format(diameterO16 * 1000 / 0.0254) + "\t" + \
          '{:.3}'.format(diameterO25 * 1000 / 0.0254) + "\t" + \
          '{:.3}'.format(diameterO34 * 1000 / 0.0254) + "\t" + \
          '{:.3}'.format(throughput * 6 / 101325 * (60 * 1000000)) + "\t\t" + \
          '{:.4}'.format(QO1) + "\t" + \
          '{:.4}'.format(QO2) + "\t" + \
          '{:.4}'.format(QO3)

for t in text:
    string = string + t + "\n"
print(string1)
plt.text(1, 0, string)
plt.ylim(0, np.mean((QO1, QO2, QO3)) * 1.75)
# plt.show()

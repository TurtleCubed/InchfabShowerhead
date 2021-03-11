import Throughput
import numpy as np
from scipy import optimize
import matplotlib
import matplotlib.pyplot as plt

# general data
temp = 298  # Kelvin
r_0 = 8.314  # in MKS


# pipe_data
# Cross-sectional shape, cross-sectional dimensions, duct length, corners, roughness
# Holes 1 and 6
shapeO16 = "cylinder"
diameterO16 = 0.039 * 0.0254
lengthO16 = 0.0625 * 0.0254
n_cO16 = 0
# Holes 2 and 5
shapeO25 = "cylinder"
diameterO25 = 0.055 * 0.0254
lengthO25 = 0.0625 * 0.0254
n_cO25 = 0
# Holes 3 and 4
shapeO34 = "cylinder"
diameterO34 = 0.079 * 0.0254
lengthO34 = 0.0625 * 0.0254
n_cO34 = 0
# Pipes Ct1 and Ct7
shapeT17 = "cylinder"
diameterT17 = 0.125 * 0.0254
lengthT17 = 0.65 * 0.0254
n_cT17 = 0
# Pipes Ct2-6
shapeT23456 = "cylinder"
diameterT23456 = 0.125 * 0.0254
lengthT23456 = 1.31 * 0.0254
n_cT23456 = 0


# gas_data
# Gamma (heat capacity ratio), molar mass, particle diameter (for mean free path), viscosity
# weighted average 2 parts Nitrogen, 8 parts Argon
gamma = 0.2 * 1.4 + 0.8 * 1.66
molar_mass = 0.2 * 0.02802 + 0.8 * 0.039948  # kg/mol
particle_diameter = (0.2 * 364 + 0.8 * 340) * 0.000000000001
viscosity = (0.2 * 1.76 + 0.8 * 2.23) * 0.00001  # Pa s


# flow_data
# Upstream pressure, downstream pressure, throughput, Reynolds number
# millitorr * 0.13332237 = pascal
p_chamber = 50 * 0.13332237
throughput = (2 + 8) * 101325 / (60 * 1000000)  # convert to Pa m^3/s
throughput = throughput / 6
re = 2300

# def throughput_p(p_upstream, p_downstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
#                  particle_diameter, viscosity, a, b, d, target, ma_n=0.15, single_run=False):
# nodeCN where N refers to the upstream pressure of the referenced pipe
nodeO1 = optimize.newton(Throughput.throughput_p, 50, args=(p_chamber, lengthO16, shapeO16, n_cO16, temp, r_0,
                                                            gamma, molar_mass, particle_diameter,
                                                            viscosity, 0, 0, diameterO16, throughput))
nodeO2 = optimize.newton(Throughput.throughput_p, 50, args=(p_chamber, lengthO25, shapeO25, n_cO25, temp, r_0,
                                                            gamma, molar_mass, particle_diameter,
                                                            viscosity, 0, 0, diameterO25, throughput))
nodeO3 = optimize.newton(Throughput.throughput_p, 50, args=(p_chamber, lengthO34, shapeO34, n_cO34, temp, r_0,
                                                            gamma, molar_mass, particle_diameter,
                                                            viscosity, 0, 0, diameterO34, throughput))
nodeT3 = optimize.newton(Throughput.throughput_p, 50, args=(nodeO3, lengthT23456, shapeT23456, n_cT23456,
                                                            temp, r_0, gamma, molar_mass,
                                                            particle_diameter, viscosity, 0, 0, diameterT23456,
                                                            throughput))
nodeT2 = optimize.newton(Throughput.throughput_p, 50, args=(nodeO2, lengthT23456, shapeT23456, n_cT23456,
                                                            temp, r_0, gamma, molar_mass,
                                                            particle_diameter, viscosity, 0, 0, diameterT23456,
                                                            throughput * 2))
nodeT1 = optimize.newton(Throughput.throughput_p, 200, args=(nodeO1, lengthT17, shapeT17, n_cT17,
                                                             temp, r_0, gamma, molar_mass,
                                                             particle_diameter, viscosity, 0, 0, diameterT17,
                                                             throughput * 3))
print('nodeO3: ', nodeO3 / 0.13332237)
print('nodeO2: ', nodeO2 / 0.13332237)
print('nodeT3 ', nodeT3 / 0.13332237)
print('difference between nodeO2 and nodeT3 (should be equal): \n', (nodeT3 - nodeO2) / 0.13332237)
print('nodeO1: ', nodeO1 / 0.13332237)
print('nodeT2 ', nodeT2 / 0.13332237)
print('difference between nodeO1 and nodeT2 (should be equal): \n', (nodeT2 - nodeO1) / 0.13332237)
print('nodeT1 ', nodeT1 / 0.13332237)


# Sensitivity Analysis
# def throughput_p(p_upstream, p_downstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
#                 particle_diameter, viscosity, a, b, d, target):

#pipe O34
diameter_rangeO34 = np.linspace(diameterO34*0.50, diameterO34*1.5)
qsO34 = np.zeros(len(diameter_rangeO34))

for i in range(len(diameter_rangeO34)):
    qsO34[i] = Throughput.throughput_p(nodeO3, p_chamber, lengthO34, shapeO34, n_cO34, temp, r_0, gamma, molar_mass,
                                       particle_diameter, viscosity, 0, 0, diameter_rangeO34[i], 0)
plt.subplot(1, 2, 1)
plt.plot(diameter_rangeO34, qsO34)

plt.show()
print(Throughput.throughput_p(nodeO3, p_chamber, lengthO34, shapeO34, n_cO34, temp, r_0, gamma, molar_mass,
                              particle_diameter, viscosity, 0, 0, diameterO34, 0))
print(Throughput.throughput_p(nodeO2, p_chamber, lengthO34, shapeO25, n_cO25, temp, r_0, gamma, molar_mass,
                              particle_diameter, viscosity, 0, 0, diameterO25, 0))
print(Throughput.throughput_p(nodeO1, p_chamber, lengthO34, shapeO16, n_cO16, temp, r_0, gamma, molar_mass,
                              particle_diameter, viscosity, 0, 0, diameterO16, 0))

import matplotlib.pyplot as plt
import GasNetworkSim
import numpy as np

shape_o = "cylinder"
diameter_o = [0.04, 0.052, 0.075]
length_o = 0.0625

shape_c = "cylinder"
diameter_c = 0.125
length_c = 1.31

throughput = 10
chamber_pressure = 50

gamma = 0.2 * 1.4 + 0.8 * 1.66  # unitless
molar_mass = 0.2 * 0.02802 + 0.8 * 0.039948  # kg/mol
particle_diameter = (0.2 * 364 + 0.8 * 340) * 10 ** -12  # m
viscosity = (0.2 * 1.76 + 0.8 * 2.23) * 10 ** -5  # Pa*s

temp = 298  # Kelvin
r_0 = 8.314  # in MKS

q = GasNetworkSim.sim_circle(shape_o, diameter_o, length_o, shape_c, diameter_c, length_c, throughput, chamber_pressure,
                             gamma, molar_mass, particle_diameter, viscosity, temp, r_0)

mean = np.mean(q)
std = np.std(q)
cv = std/mean
print(cv)
import Throughput
import numpy as np
from scipy import optimize
import matplotlib
import matplotlib.pyplot as plt
import pyperclip
import GasNetworkSim

# Provide these dimensions in INCHES!!!
# Opening dimensions
shape_o = "rectangle"
width_o = 0.050
height_o = [0.028, 0.032, 0.040]
length_o = 0.0625
# Connecting pipe dimensions
shape_c = "circle"
diameter_c = 0.1875
length_c = 2.25

# Provide flow in SCCM!!!
throughput = 150
# Provide pressure in MILLITORR!!!
chamber_pressure = 50

# Gas data
# Weighted average of 0.2 N2 and 0.8 Ar
gamma = 1.667  # unitless
molar_mass = 0.004  # kg/mol
particle_diameter = 260 * 10 ** -12  # m
viscosity = 1.96 * 10 ** -5  # Pa*s

# general data
temp = 298  # Kelvin
r_0 = 8.314  # in MKS


q = GasNetworkSim.sim(shape_o, height_o, width_o, length_o, shape_c, diameter_c, 0.0, length_c, throughput,
                      chamber_pressure, gamma, molar_mass, particle_diameter, viscosity, temp, r_0)
print(q)

"""
This script compares the throughput coming out of each opening by first assuming some inlet pressure, then correcting
that assumption using the chamber pressure.
"""
import Throughput
import numpy as np
from scipy import optimize
import matplotlib
import matplotlib.pyplot as plt
import pyperclip

# Provide these dimensions in INCHES!!!
# Opening dimensions
shape_o = "cylinder"
diameter_o = [0.032, 0.037, 0.045, 0.060, 0.088]
length_o = 0.0625
# Connecting pipe dimensions
shape_c = "cylinder"
diameter_c = 0.125
length_c = 0.786

# Provide flow in SCCM!!!
throughput = 10
# Provide pressure in MILLITORR!!!
chamber_pressure = 50

# Gas data
# Weighted average of 0.2 N2 and 0.8 Ar
gamma = 0.2 * 1.4 + 0.8 * 1.66  # unitless
molar_mass = 0.2 * 0.02802 + 0.8 * 0.039948  # kg/mol
particle_diameter = (0.2 * 364 + 0.8 * 340) * 10 ** -12  # m
viscosity = (0.2 * 1.76 + 0.8 * 2.23) * 10 ** -5  # Pa*s

# general data
temp = 298  # Kelvin
r_0 = 8.314  # in MKS

# Convert all values to MKS
diameter_c = diameter_c * 0.0254
length_c = length_c * 0.0254
diameter_o = [i * 0.0254 for i in diameter_o]
length_o = length_o * 0.0254
throughput = throughput * 101325 / (60 * 10 ** 6)
chamber_pressure = chamber_pressure * 0.13332237

# Obtaining an inlet pressure guess
p_guesses = [None] * len(diameter_o)
for i in range(len(diameter_o)):
    p_up = optimize.newton(Throughput.throughput_p, chamber_pressure * 8, args=(
        chamber_pressure, length_o, shape_o, 0, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0,
        diameter_o[i], throughput / (len(diameter_o) * 2)))
    for j in range(i, -1, -1):
        length = length_c
        if j == 0:
            length = length / 2
        q_temp = throughput * (len(diameter_o) - j) / (2 * len(diameter_o))
        p_up = optimize.newton(Throughput.throughput_p, p_up * 5, args=(
            p_up, length, shape_c, 0, temp, r_0, gamma, molar_mass, particle_diameter, viscosity, 0, 0, diameter_c,
            q_temp))
    p_guesses[i] = p_up

# p_up = np.mean(p_guesses)


def find_p(p_guess):
    p_up = p_guess
    p = [None] * len(diameter_o)
    q = throughput / 2
    opening_q = [None] * len(diameter_o)

    for i in range(len(diameter_o)):
        length = length_c
        if i is 0:
            length = length_c / 2
        p[i] = Throughput.downstream_pressure(p_up, q, length, shape_c, 0, temp, r_0, gamma,
                                              molar_mass, particle_diameter, viscosity, 0, 0, diameter_c,
                                              p_down=chamber_pressure)
        if i is not len(diameter_o) - 1:
            opening_q[i] = Throughput.throughput_p(p[i], chamber_pressure, length_o, shape_o, 0, temp, r_0, gamma,
                                                   molar_mass,
                                                   particle_diameter, viscosity, 0, 0, diameter_o[i], 0)
            q = q - opening_q[i]
        else:
            opening_q[i] = q
        p_up = p[i]

    p_ref = optimize.newton(Throughput.throughput_p, chamber_pressure * 1.2,
                            args=(chamber_pressure, length_o, shape_o, 0, temp, r_0,
                                  gamma, molar_mass, particle_diameter, viscosity,
                                  0, 0, diameter_o[len(diameter_o) - 1],
                                  opening_q[len(opening_q) - 1]))
    return p_ref - p[len(p)-1]


correct_p = optimize.newton(find_p, np.mean(p_guesses))
p_up = correct_p

p = [None] * len(diameter_o)
q = throughput / 2
opening_q = [None] * len(diameter_o)

for i in range(len(diameter_o)):
    length = length_c
    if i is 0:
        length = length_c / 2
    p[i] = Throughput.downstream_pressure(p_up, q, length, shape_c, 0, temp, r_0, gamma,
                                          molar_mass, particle_diameter, viscosity, 0, 0, diameter_c,
                                          p_down=chamber_pressure)
    if i is not len(diameter_o) - 1:
        opening_q[i] = Throughput.throughput_p(p[i], chamber_pressure, length_o, shape_o, 0, temp, r_0, gamma,
                                               molar_mass,
                                               particle_diameter, viscosity, 0, 0, diameter_o[i], 0)
        q = q - opening_q[i]
    else:
        opening_q[i] = q
    p_up = p[i]

p_ref = optimize.newton(Throughput.throughput_p, chamber_pressure * 1.2,
                        args=(chamber_pressure, length_o, shape_o, 0, temp, r_0,
                              gamma, molar_mass, particle_diameter, viscosity,
                              0, 0, diameter_o[len(diameter_o) - 1],
                              opening_q[len(opening_q) - 1]))

for i in opening_q:
    print(i * (101325 / (60 * 10 ** 6)) ** -1)

print("determined pressure = ", p[len(p) - 1])
print("reference pressure = ", p_ref)

x = range(len(diameter_o))
x = [a + 1 for a in x]
y = [a * (101325 / (60 * 10 ** 6)) ** -1 for a in opening_q]
means = np.ones(len(opening_q)) * np.mean(y)
plt.title("Throughput at Each Opening")
plt.xticks(x, x)
plt.xlabel("Opening Number")
plt.ylabel("Throughput (MKS)")
plt.plot(x, y)
plt.plot(x, means)

for i in range(len(opening_q)):
    label = '{:.4}'.format(y[i]) + " SCCM"
    plt.text(i + 1, y[i] + np.mean(y) * 0.1, label)

text = []
text.append("Net throughput: " + '{:.3}'.format(throughput / 101325 * (60 * 1000000)))
text.append("Aperture length: " + '{:.3}'.format(length_o * 1000 / 0.0254) + " mil")
for i in range(len(opening_q)):
    text.append("Diameter O" + str(i + 1) + ": " + '{:.3}'.format(diameter_o[i] * 1000 / 0.0254) + " mil")
text.append("Connecting Pipe Diameter: " + '{:.3}'.format(diameter_c * 1000 / 0.0254) + " mil")
string = ""
for t in text:
    string = string + t + "\n"
plt.text(1, 0, string)
plt.ylim(0, np.mean(y) * 1.75)
# plt.show()

text1 = [str(round(1000 * length_o / 0.0254, 3))]
for i in range(len(diameter_o)):
    text1.append(str(round(1000 * diameter_o[i] / 0.0254, 2)))
text1.append(str(throughput / 101325 * (60 * 1000000)))
text1.append('')
for i in range(len(y)):
    text1.append(str(round(y[i], 3)))
for i in range(len(y)):
    text1.append((str(round((y[i] - np.mean(y)) * 100 / np.mean(y), 3))))
text1.append(str(round(np.std(y)/np.mean(y), 4)))
text2 = ""
for string1 in text1:
    print(string1, '\t', end='')
    text2 = text2 + string1 + '\t'

pyperclip.copy(text2)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import GasNetworkSim
import numpy as np
import concurrent.futures


def sims(num, list0):
    successful_runs = []
    for i in range(len(list0)):
        if (i - num) % 12 is 0:
            print(list0[i])
            try:
                q = GasNetworkSim.sim_circle(shape_o, list0[i], length_o, shape_c, diameter_c, length_c, throughput,
                                             chamber_pressure,
                                             gamma, molar_mass, particle_diameter, viscosity, temp, r_0)
                mean = np.mean(q)
                std = np.std(q)
                cv = std / mean
                if cv < 0.01:
                    successful_runs.append((list0[i][0], list0[i][1], list0[i][2], cv))
            except ValueError and RuntimeError:
                print(list_to_run[i], 'not valid')
    return successful_runs


shape_o = "cylinder"
diameter_o = [0.04, 0.053, 0.079]
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

d1 = np.linspace(0.039, 0.041, 3)
d2 = np.linspace(0.052, 0.054, 3)
d3 = np.linspace(0.078, 0.080, 3)

runs = len(d1) * len(d2) * len(d3)
count = 1
list_to_run = []
success_list = []

for i in d1:
    for j in d2:
        for k in d3:
            list_to_run.append([i, j, k])

threads = [None]*12
with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(12):
        threads[i] = executor.submit(sims, i, list_to_run)
    for t in threads:
        if len(t.result()) > 1:
            success_list.append(t.result())


d1s = [a[0] for a in success_list]
d2s = [a[1] for a in success_list]
d3s = [a[2] for a in success_list]
cvs = [a[3] for a in success_list]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
img = ax.scatter(d1s, d2s, d3s, c=cvs, cmap='Reds_r')
fig.colorbar(img)
for i in range(len(cvs)):
    ax.text(d1s[i], d2s[i], d3s[i], cvs[i])
plt.show()

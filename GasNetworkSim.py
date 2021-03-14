import Throughput
import numpy as np
from scipy import optimize


def sim(shape_o, dim_o, width_o, length_o, shape_c, dim_c, width_c, length_c, throughput, chamber_pressure,
        gamma, molar_mass, particle_diameter, viscosity, temp, r_0):
    # Convert all values to MKS
    dim_o = [i * 0.0254 for i in dim_o]
    width_o *= 0.0254
    length_o *= 0.0254
    dim_c *= 0.0254
    width_c *= 0.0254
    length_c *= 0.0254
    throughput = throughput * 101325 / (60 * 10 ** 6)
    chamber_pressure *= 0.13332237

    # Obtaining an inlet pressure guess
    p_guesses = [None] * len(dim_o)
    for i in range(len(dim_o)):
        args1 = (chamber_pressure, length_o, shape_o, 0, temp, r_0, gamma, molar_mass, particle_diameter,
                 viscosity, dim_o[i], width_o, dim_o[i], throughput / (len(dim_o) * 2))
        p_up = optimize.newton(Throughput.throughput_p, chamber_pressure * 8, args=args1)
        for j in range(i, -1, -1):
            length = length_c
            if j == 0:
                length = length / 2
            q_temp = throughput * (len(dim_o) - j) / (2 * len(dim_o))
            args1 = (p_up, length, shape_c, 0, temp, r_0, gamma, molar_mass, particle_diameter, viscosity,
                     dim_c, width_c, dim_c, q_temp)
            p_up = optimize.newton(Throughput.throughput_p, p_up * 5, args=args1)
        p_guesses[i] = p_up

    # p_up = np.mean(p_guesses)

    def find_p(p_guess):
        p_up = p_guess
        p = [None] * len(dim_o)
        q = throughput / 2
        opening_q = [None] * len(dim_o)

        for i in range(len(dim_o)):
            length = length_c
            if i is 0:
                length = length_c / 2
            p[i] = Throughput.downstream_pressure(p_up, q, length, shape_c, 0, temp, r_0, gamma,
                                                  molar_mass, particle_diameter, viscosity, dim_c, width_c, dim_c,
                                                  p_down=chamber_pressure)
            if i is not len(dim_o) - 1:
                opening_q[i] = Throughput.throughput_p(p[i], chamber_pressure, length_o, shape_o, 0, temp, r_0, gamma,
                                                       molar_mass, particle_diameter, viscosity, dim_o[i], width_o,
                                                       dim_o[i], 0)
                q = q - opening_q[i]
            else:
                opening_q[i] = q
            p_up = p[i]

        p_ref = optimize.newton(Throughput.throughput_p, chamber_pressure * 1.2,
                                args=(chamber_pressure, length_o, shape_o, 0, temp, r_0, gamma, molar_mass,
                                      particle_diameter, viscosity, dim_o[len(dim_o) - 1], width_o,
                                      dim_o[len(dim_o) - 1], opening_q[len(opening_q) - 1]))
        return p_ref - p[len(p) - 1]

    correct_p = optimize.newton(find_p, np.mean(p_guesses))
    p_up = correct_p

    p = [None] * len(dim_o)
    q = throughput / 2
    opening_q = [None] * len(dim_o)

    for i in range(len(dim_o)):
        length = length_c
        if i is 0:
            length = length_c / 2
        p[i] = Throughput.downstream_pressure(p_up, q, length, shape_c, 0, temp, r_0, gamma,
                                              molar_mass, particle_diameter, viscosity, dim_c, width_c, dim_c,
                                              p_down=chamber_pressure)
        if i is not len(dim_o) - 1:
            opening_q[i] = Throughput.throughput_p(p[i], chamber_pressure, length_o, shape_o, 0, temp, r_0, gamma,
                                                   molar_mass, particle_diameter, viscosity, dim_o[i], width_o,
                                                   dim_o[i], 0)
            q = q - opening_q[i]
        else:
            opening_q[i] = q
        p_up = p[i]

    return opening_q

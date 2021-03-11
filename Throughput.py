import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def downstream_pressure(p_upstream, throughput, length, shape, n_c, temp, r_0, gamma, mol_mass,
                        particle_diameter, viscosity, a, b, d, p_down=0.0):
    debug = False
    if debug:
        try:
            zero = optimize.root_scalar(throughput_pd, bracket=[p_down, p_upstream * 0.999],
                                        args=(p_upstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
                                              particle_diameter, viscosity, a, b, d, throughput), method='brentq')
        except ValueError:
            ps = np.linspace(p_down, p_upstream * 0.999, 100)
            throughs = [None] * len(ps)
            for i in range(len(ps)):
                throughs[i] = throughput_pd(ps[i], p_upstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
                                            particle_diameter, viscosity, a, b, d, throughput)
            plt.plot(ps, throughs)
            plt.show()
            quit()
    else:
        zero = optimize.root_scalar(throughput_pd, bracket=[p_down, p_upstream * 0.999],
                                    args=(p_upstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
                                          particle_diameter, viscosity, a, b, d, throughput), method='brentq')
    return zero.root


def throughput_p(p_upstream, p_downstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
                 particle_diameter, viscosity, a, b, d, target):
    re_old = 300
    q, re_new = throughput(re_old, p_upstream, p_downstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
                           particle_diameter, viscosity, a, b, d, single_run=True)
    while abs((re_new - re_old) / re_new) > 0.001:
        re_old = re_new
        q, re_new = throughput(re_old, p_upstream, p_downstream, length, shape, n_c, temp, r_0, gamma,
                               mol_mass, particle_diameter, viscosity, a, b, d, single_run=True)
    return q - target


def throughput_pd(p_downstream, p_upstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
                  particle_diameter, viscosity, a, b, d, target):
    re_old = 30
    q, re_new = throughput(re_old, p_upstream, p_downstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
                           particle_diameter, viscosity, a, b, d, single_run=True)
    while abs((re_new - re_old) / re_new) > 0.001:
        re_old = re_new
        q, re_new = throughput(re_old, p_upstream, p_downstream, length, shape, n_c, temp, r_0, gamma,
                               mol_mass, particle_diameter, viscosity, a, b, d, single_run=True)
    return q - target


def throughput_d(d, p_upstream, p_downstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
                 particle_diameter, viscosity, a, b, target):
    re_old = 300
    q, re_new = throughput(re_old, p_upstream, p_downstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
                           particle_diameter, viscosity, a, b, d, single_run=True)
    while abs((re_new - re_old) / re_new) > 0.001:
        re_old = re_new
        q, re_new = throughput(re_old, p_upstream, p_downstream, length, shape, n_c, temp, r_0, gamma,
                               mol_mass, particle_diameter, viscosity, a, b, d, single_run=True)
    return q - target


def throughput(r_e, p_upstream, p_downstream, length, shape, n_c, temp, r_0, gamma, mol_mass,
               particle_diameter, viscosity, a, b, d, ma_n=0.15, single_run=False):
    if shape is "circle":
        radius = d / 2
        area = np.pi * np.power(radius, 2)
        perimeter = np.pi * d
        d_h = 4 * area / perimeter
        le = length * (1 + 1 / (3 + 3 * length / (7 * radius)))
        alpha = 1 / (1 + 3 * le / (8 * radius))
        ge = np.power(perimeter, 4) / (128 * np.power(np.pi, 3))
    elif shape is "rectangle":
        area = a * b
        perimeter = 2 * (a + b)
        d_h = 4 * area / perimeter
        r = b / a
        r_max = 0.025 * np.power(length / a, 2) + (length / a) + 55
        if r > r_max:
            r = r_max
        x = np.sqrt(np.power(r, 2) - 1) / r
        u = length / (0.5 * d_h + length)
        v = r / np.sqrt((1-u) * np.power(r, 1.5) + u)
        w = (16/(3 * np.power(np.pi, 1.5)) * np.log(4*v + ((0.72+x)/v)))
        le = length * (1+(1/(4+((4*length)/(7*a)))))
        alpha = w / ((le/a) + w)
        ge = (1/12) * (np.power(a*b, 3))/(np.power(a, 2) + np.power(b, 2) + 0.371*a*b)
    elif shape is "annulus":
        # Probably not todo
        area = 0
        perimeter = 0
        d_h = 4 * area / perimeter
        alpha = 0
        ge = 0
    else:
        area = 0
        perimeter = 0
        d_h = 4 * area / perimeter
        alpha = 0
        ge = 0
    s_f = np.power(area, 3) / (2 * np.power(perimeter, 2) * ge)
    f_d = 64 / (r_e / s_f)

    # Determine if flow is choked or not
    l_c = length + 0.41 * d_h
    # def ma_n_helper(ma_n, f_d, gamma, ma_x, n_c, l_c, d_h):
    # ma_n = optimize.newton(ma_n_helper, ma_n, args=(f_d, gamma, 1, n_c, l_c, d_h), maxiter=1000)
    try:
        zero = optimize.root_scalar(ma_n_helper, bracket=[10 ** -6, 1], args=(f_d, gamma, 1, n_c, l_c, d_h),
                                    method='brentq')
        ma_n = zero.root
    except ValueError:
        try:
            ma_n = optimize.newton(ma_n_helper, ma_n, args=(f_d, gamma, 1, n_c, l_c, d_h))
        except RuntimeError:
            mans = np.linspace(0.001, 1, 100)
            ys = ma_n_helper(mans, f_d, gamma, 1, n_c, l_c, d_h)
            fig, ax = plt.subplots()
            ax.plot(mans, ys)
            ax.set(xlabel='man guess', ylabel='helper',
                   title='for debugging mans')
            ax.grid()
            plt.show()
            quit()

    temp1 = (1 / ma_n) * np.power((gamma + 1) / 2, 1 / 2)
    temp2 = 1 + ((1 / 2) * (gamma - 1) * np.power(ma_n, 2))
    temp3 = (gamma + 1) / (2 * (gamma - 1))
    k_choked = temp1 * np.power(temp2, temp3)

    k_c_pressures = p_upstream / p_downstream
    choked = k_c_pressures >= k_choked

    # Solving for viscous flow component of throughput
    t_0 = temp * (1 + (gamma - 1)/2 * np.power(ma_n, 2))  # Stagnation temperature
    c_z = area * np.sqrt(r_0 * t_0 / mol_mass)
    if choked:
        temp1 = gamma * (gamma + 1) / 2
        temp2 = c_z * p_upstream / k_choked
        qv = np.sqrt(temp1) * temp2
    else:
        #def ma_n_helper_unchoked(ma_n, f_d, gamma, n_c, l_c, d_h, p_up, p_down):
        temptest = ma_n_helper_unchoked(10**-6, f_d, gamma, n_c, l_c, d_h, p_upstream, p_downstream)
        temptest1 = ma_n_helper_unchoked(1, f_d, gamma, n_c, l_c, d_h, p_upstream, p_downstream)

        zero = optimize.root_scalar(ma_n_helper_unchoked, bracket=[10 ** -6, 1], args=(f_d, gamma, n_c, l_c, d_h,
                                                                                       p_upstream, p_downstream),
                                    method='brentq')
        ma_n = zero.root
        temp1 = 1 + 0.5 * (gamma - 1) * np.power(ma_n, 2)
        temp2 = (gamma + 1) / (2 * (gamma - 1))
        qv = np.sqrt(gamma) * c_z * p_upstream * ma_n / (np.power(temp1, temp2))

    # Solving for molecular flow component of throughput
    c_a = area * np.sqrt(r_0 * t_0 / (2 * np.pi * mol_mass))
    qm = c_a * alpha * (p_upstream - p_downstream)

    # Qm total requires solving for phi
    # which requires solving for the mean free path
    p_ave = (p_upstream + p_downstream) / 2
    n_a = 6.0221367 * np.power(10.0, 23)
    temp1 = r_0 * temp
    temp2 = np.sqrt(2) * np.pi * particle_diameter * particle_diameter * n_a * p_ave
    mean_free_path = temp1 / temp2
    kn = mean_free_path / d_h
    phi_s = 3 * np.pi / (128 * kn)
    phi_l = (3 * np.pi * (1 + 4 * kn)) / (128 * (1 + kn) * np.power(kn, 0.55))
    phi = phi_s + ((phi_l - phi_s) * length / (length + d_h))

    q = qv + (qm / (1+phi))
    re_new = 4 * mol_mass * q / (r_0 * t_0 * perimeter * viscosity)
    if single_run:
        return q, re_new
    else:
        return q


def ma_n_helper(ma_n, f_d, gamma, ma_x, n_c, l_c, d_h):
    temp1 = n_c + (f_d * l_c) / d_h
    temp2 = (1 / np.power(ma_n, 2)) - (1 / np.power(ma_x, 2))
    temp3 = (gamma + 1) / 2
    temp4 = np.power((ma_x / ma_n), 2) * ((gamma - 1) * np.power(ma_n, 2) + 2) / ((gamma - 1) * np.power(ma_x, 2) + 2)
    return (1/gamma) * (temp2 - temp3 * np.log(temp4)) - temp1


def ma_n_helper_unchoked(ma_n, f_d, gamma, n_c, l_c, d_h, p_up, p_down):
    k = p_up / p_down
    power = (gamma + 1) / (gamma - 1)
    num = 2 * (gamma-1) * np.power(k, 2) * np.power(ma_n, 2)
    den = np.power(1 + (1/2) * (gamma-1) * np.power(ma_n, 2), power)
    ma_x = np.sqrt((np.sqrt(1 + num/den) - 1)/(gamma-1))

    temp1 = n_c + (f_d * l_c) / d_h
    temp2 = (1 / (np.power(ma_n, 2))) - (1 / (np.power(ma_x, 2)))
    temp3 = (gamma + 1) / 2
    temp4 = np.power((ma_x / ma_n), 2) * ((gamma - 1) * np.power(ma_n, 2) + 2) / ((gamma - 1) * np.power(ma_x, 2) + 2)
    return (1/gamma) * (temp2 - temp3 * np.log(temp4)) - temp1




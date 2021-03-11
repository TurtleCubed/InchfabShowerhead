from scipy import optimize
import numpy as np


def ma_n_helper(ma_n, f_d, gamma, ma_x, n_c, l_c, d_h):
    a = n_c + (f_d * l_c) / d_h
    b = (1 / (np.power(ma_n, 2))) - (1 / (np.power(ma_x, 2)))
    c = (gamma + 1) / 2
    d = np.power((ma_x / ma_n), 2) * ((gamma - 1) * np.power(ma_n, 2) + 2) / ((gamma - 1) * np.power(ma_x, 2) + 2)
    return (1/gamma) * (b - c * np.log(d)) - a


def find_ma_n(man0, fd, gamma, max, nc, l_c, d_h):
    return optimize.newton(ma_n_helper, man0, args=(fd, gamma, max, nc, l_c, d_h))


def ma_n_helper_unchoked(ma_n, f_d, gamma, n_c, l_c, d_h, p_up, p_down):
    k = p_up / p_down
    num = 2 * (gamma-1) * np.power(k, 2) * np.power(ma_n, 2)
    den = np.power(1 + (1/2) * (gamma-1)*np.power(ma_n, 2), (gamma+1)/(gamma-1))
    ma_x = np.sqrt((np.sqrt(1 + num/den) - 1)/(gamma-1))

    a = n_c + (f_d * l_c) / d_h
    b = (1 / (np.power(ma_n, 2))) - (1 / (np.power(ma_x, 2)))
    c = (gamma + 1) / 2
    d = np.power((ma_x / ma_n), 2) * ((gamma - 1) * np.power(ma_n, 2) + 2) / ((gamma - 1) * np.power(ma_x, 2) + 2)
    return (1/gamma) * (b + c * np.log(d)) - a


def find_ma_n_unchoked(man0, fd, gamma, n_c, l_c, d_h, p_up, p_down):
    return optimize.newton(ma_n_helper_unchoked, man0, args=(fd, gamma, n_c, l_c, d_h, p_up, p_down))


def k_choked(man0, gamma):
    a = (1/man0) * np.power((gamma+1)/2, 1/2)
    b = 1 + ((1/2)*(gamma-1)*np.power(man0, 2))
    c = (gamma+1)/(2*(gamma-1))
    return a * np.power(b, c)


def is_choked(p_upstream, p_x, man0, gamma):
    k_c_man = k_choked(man0, gamma)
    k_c_pressures = p_upstream / p_x
    if k_c_pressures >= k_c_man:
        return True


def c_z(area, r_0, t_0, molar_mass):
    return area * np.sqrt(r_0 * t_0 / molar_mass)


def q_v(choked, gamma, c_z, p_u, k_c=0, ma_n=0):
    if choked:
        a = gamma * (gamma + 1) / 2
        b = c_z * p_u / k_c
        q = np.sqrt(a) * b
    else:
        a = 1 + 0.5 * (gamma-1) * np.power(ma_n, 2)
        b = (gamma+1) / (2 * (gamma-1))
        q = np.sqrt(gamma) * c_z * p_u * ma_n / (np.power(a, b))
    return q


def q(q_c, q_m, phi):
    return q_c + (q_m / (1+phi))


def q_m(c_a, alpha, p_upstream, p_downstream):
    return c_a * alpha * (p_upstream - p_downstream)


def c_a(area, R_0, temp, molar_mass):
    return area * np.sqrt(R_0 * temp / (2*np.pi*molar_mass))


def alpha(radius, length):
    le = length * (1 + 1 / (3 + 3 * length / (7*radius)))
    return 1 / (1 + 3 * le / (8*radius))


def phi(kn, length, d_h):
    phi_s = 3 * np.pi / (128 * kn)
    phi_l = (3*np.pi*(1+4*kn)) / (128*(1+kn)*np.power(kn, 0.55))
    return phi_s + ((phi_l - phi_s) * length / (length + d_h))


def kn(lamb, d_h):
    return lamb / d_h


def mean_free_path(R_0, temp, particle_diameter, pressure):
    n_a = 6.0221367 * np.power(10.0, 23)
    nume = R_0 * temp
    deno = np.sqrt(2) * np.pi * particle_diameter * particle_diameter * n_a * pressure
    return nume / deno


def re(molar_mass, q, r, temp, perimeter, viscosity):
    return 4 * molar_mass * q / (r * temp * perimeter * viscosity)



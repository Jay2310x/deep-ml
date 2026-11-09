import numpy as np


# -------------------- KERNELS --------------------

def rbf_kernel(x, x_prime, sigma=1.0, length_scale=1.0):
    sq_dist = np.sum((x - x_prime) ** 2)
    return sigma**2 * np.exp(-0.5 * sq_dist / length_scale**2)


def linear_kernel(x, x_prime, sigma_b=1.0, sigma_v=1.0):
    return sigma_b**2 + sigma_v**2 * np.dot(x, x_prime)


def matern_kernel(x, x_prime, length_scale=1.0, nu=1.5, sigma=1.0):
    r = np.sqrt(np.sum((x - x_prime) ** 2))
    if nu == 1.5:
        factor = (1 + np.sqrt(3) * r / length_scale)
        return sigma**2 * factor * np.exp(-np.sqrt(3) * r / length_scale)
    else:
        return sigma**2 * np.exp(-r / length_scale)


def periodic_kernel(x, x_prime, sigma=1.0, length_scale=1.0, period=1.0):
    r = np.sqrt(np.sum((x - x_prime) ** 2))
    return sigma**2 * np.exp(
        -2 * (np.sin(np.pi * r / period) ** 2) / length_scale**2
    )


def rational_quadratic_kernel(x, x_prime, sigma=1.0, length_scale=1.0, alpha=1.0):
    sq_dist = np.sum((x
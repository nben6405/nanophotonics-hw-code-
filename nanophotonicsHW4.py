import numpy as np
import matplotlib.pyplot as plt

lam = np.linspace(500, 600, 50000)  # wavelength in nm
L = 10e-6                            # slab thickness in m

def fp(lam_nm, n):
    r = (1 - n) / (1 + n)
    delta = 2 * np.pi * n * L / (lam_nm * 1e-9)
    denom = (1 - r**2)**2 + 4 * r**2 * np.sin(delta)**2
    R = 4 * r**2 * np.sin(delta)**2 / denom
    T = (1 - r**2)**2 / denom
    return T, R

for n in [1.45, 3.45]:
    T, R = fp(lam, n)

    # Find peaks manually: points higher than both neighbors
    peaks = np.where((R[1:-1] > R[:-2]) & (R[1:-1] > R[2:]))[0] + 1

    # Peak nearest to 560 nm
    idx = peaks[np.argmin(np.abs(lam[peaks] - 560))]
    left  = np.where(R[:idx] < R[idx]/2)[0][-1]
    right = idx + np.where(R[idx:] < R[idx]/2)[0][0]
    Q = lam[idx] / (lam[right] - lam[left])
    print(f"n={n}: lambda_res={lam[idx]:.2f} nm, FWHM={lam[right]-lam[left]:.4f} nm, Q={Q:.1f}")

    plt.figure()
    plt.plot(lam, T, label='T')
    plt.plot(lam, R, label='R')
    plt.title(f'n={n}, Q≈{Q:.1f}')
    plt.xlabel('Wavelength (nm)')
    plt.legend()
    plt.savefig(f'fp_n{n}.png', dpi=150)

plt.show()
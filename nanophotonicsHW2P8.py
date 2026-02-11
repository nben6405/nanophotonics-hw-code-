import matplotlib.pyplot as plt
import numpy as np

# constants
wp = 2.4e16
gamma = 1.1e15
c = 3e8

# wavelength regime // lambda
w_len_nm = np.linspace(200, 600, 50)
w_len_m = np.linspace(200, 600, 50)*1e-9

# omega
w = 2* np.pi * c / w_len_m


# drude model // relative permittivity of aluminum
drude = 1 - ((wp**2)/(w**2 + 1j*gamma*w))

plt.figure()
plt.plot(w_len_nm, drude.real, label="Real Permittivity")
plt.plot(w_len_nm, drude.imag, label="Imaginary Permittivity")
plt.xlabel("Wavelength (m)")
plt.ylabel("Relative Permittivity of Aluminum")
plt.title("Aluminum Permittivity")


plt.tight_layout()
plt.show()



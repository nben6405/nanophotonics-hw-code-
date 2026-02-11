'''
N. Ben Ari
(2) plotting R & T vs incident angle ranging from 0 to 90 degrees
(3) same as (2) , but with a different set of material properties

'''

import numpy as np
import matplotlib.pyplot as plt

#(2)
# material properties
epsilon1 = 1.0
mu1 = 1.0
epsilon2 = 6.25
mu2 = 1.0

#(3)
# material properties
'''epsilon1_3 = 6.25
mu1_3 = 1.0
epsilon2_3 = 1.0
mu2_3 = 1.0'''

theta_i_deg = np.linspace(0, 90, 1000) #incident angle 0 --> 90 degrees
theta_i_rad = np.deg2rad(theta_i_deg) #incident angle in rads

#snell's law for transmitted angle
n1 = np.sqrt(epsilon1 * mu1)
n2 = np.sqrt(epsilon2 * mu2)
theta_t_rad = np.arcsin((n1/n2) * (np.sin(theta_i_rad)))

kz1 = n1 * np.cos(theta_i_rad)
kz2 = n2 * np.cos(theta_t_rad)

rs = (mu2 * kz1 - mu1 * kz2) / (mu2 * kz1 + mu1 * kz2)
ts = (2 * mu2 * kz1) / (mu2 * kz1 + mu1 * kz2)
rp = (epsilon2 * kz1 - epsilon1 * kz2) / (epsilon2 * kz1 + epsilon1 * kz2)
tp = ((2 * epsilon2 * kz1) / (epsilon2 * kz1 + epsilon1 * kz2)) * np.sqrt((mu2 * epsilon1) / (mu1 * epsilon2))

Rs = np.abs(rs)**2
Rp = np.abs(rp)**2

Ts = np.sqrt((epsilon2 * mu1) / (epsilon1 * mu2)) * (np.cos(theta_t_rad) / np.cos(theta_i_rad)) * np.abs(ts)**2
Tp = np.sqrt((epsilon2 * mu1) / (epsilon1 * mu2)) * (np.cos(theta_t_rad) / np.cos(theta_i_rad)) * np.abs(tp)**2


#plotting
fig, ax = plt.subplots(1, 2, figsize=(12,5))

# Reflectance Plot
ax[0].plot(theta_i_deg, Rs, label=r'$R^s$ (TE)', color='blue')
ax[0].plot(theta_i_deg, Rp, label=r'$R^p$ (TM)', color='red')
ax[0].set_title('Reflectance (R)')
ax[0].set_xlabel('Incident Angle (degrees)')
ax[0].set_ylabel('Reflectance')
ax[0].grid(True)
ax[0].legend()

# Transmittance Plot
ax[1].plot(theta_i_deg, Ts, label=r'$T^s$ (TE)', color='blue')
ax[1].plot(theta_i_deg, Tp, label=r'$T^p$ (TM)', color='red')
ax[1].set_title('Transmittance (T)')
ax[1].set_xlabel('Incident Angle (degrees)')
ax[1].set_ylabel('Transmittance')
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()

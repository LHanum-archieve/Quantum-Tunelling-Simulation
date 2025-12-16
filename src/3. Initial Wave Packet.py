# 3. Initial Wave Packet (Gaussian) 
x0         = 20.0          # Initial center of the packet
sigma      = 5.0           # Width of the Gaussian
k0         = 6             # Incident wave number (Momentum: p0 = hbar * k0)
E_incident = (hbar * k0)**2 / (2 * m)

# Normalization factor for probability density integral = 1
A          = (1 / (2 * np.pi * sigma**2))**0.25
psi0       = A * np.exp(-(x - x0)**2 / (4 * sigma**2)) * np.exp(1j * k0 * x)
psi        = psi0


# 4. Split-Step Fourier Method (TDSE Solver)
# Pre-calculate k-space operator
k           = 2 * np.pi * np.fft.fftfreq(N, d=dx)
kinetic_exp = np.exp(-1j * hbar * k**2 / (2 * m) * dt)

def time_step(psi):
    # Half-step Potential
    psi   = psi * np.exp(-1j * V * (dt / 2) / hbar)
    # Full-step Kinetic Energy
    psi_k = np.fft.fft(psi)
    psi_k = psi_k * kinetic_exp
    psi   = np.fft.ifft(psi_k)
    # Second Half-step Potential
    psi   = psi * np.exp(-1j * V * (dt / 2) / hbar)
    return psi

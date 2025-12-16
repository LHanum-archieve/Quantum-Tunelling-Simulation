import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Simulation Setup (Scaled Units for Visualization)
N               = 512                   # Number of spatial grid points
L               = 100                   # Length of the simulation box (arbitrary units)
dx              = L / N                 # Spatial step size
x               = np.linspace(0, L, N)  # Spatial grid

# Time parameters
T_final        = 11.0                   # Final time of simulation
dt             = 0.005                  # Time step size
n_steps        = int(T_final / dt)
frames_per_sec = 20                     # Desired frames per second for the animation

# Calculate the step interval to save frames efficiently
step_interval  = max(1, int(n_steps / (frames_per_sec * T_final)))

# Particle properties (Scaled)
hbar           = 1.0                    # Reduced Planck's constant
m              = 1.0                    # Mass of the particle

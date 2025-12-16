# 2. Potential Barrier V(x)
V0      = 10.0       # Barrier height
a       = 5.0        # Barrier width
x_start = 50.0       # Barrier starting position

# Define the potential array
V       = np.zeros(N)
V[(x >= x_start) & (x <= x_start + a)] = V0


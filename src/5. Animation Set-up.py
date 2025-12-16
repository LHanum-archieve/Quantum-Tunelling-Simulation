# 5. Animation Setup (Time evolution and saving frames) 
# List to store the probability density (for animation frames)
history = []

# Perform the time evolution and store frames
current_psi = psi.copy()
for i in range(n_steps):
    current_psi = time_step(current_psi)
    if i % step_interval == 0:
        # Store the probability density: P(x,t) = |psi(x,t)|^2
        history.append(np.abs(current_psi)**2)

print(f"Calculated {len(history)} frames for animation.")

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the potential barrier (static part)
ax.plot(x, V, 'r--', label=f'Potential Barrier ($V_0={V0:.1f}$)')
ax.fill_between(x, 0, V, color='red', alpha=0.1)

# Initialize the wave function plot (dynamic part)
line, = ax.plot(x, history[0], 'b-', label=r'$|\Psi(x,t)|^2$')

# Title and labels setup
ax.set_title(f'Quantum Tunneling Simulation (Energy $E={E_incident:.2f}$, $V_0={V0:.1f}$)')
ax.set_xlabel('Position (x)')
ax.set_ylabel('Probability Density')
ax.set_xlim(0, L)
ax.set_ylim(0, np.max(history[0]) * 1.1)
ax.legend(loc='upper right')
ax.grid(True)

def update(frame):
    """Update function for the animation."""
    line.set_ydata(history[frame])
    ax.set_title(f'Quantum Tunneling Simulation (Time $t={frame * dt * step_interval:.2f}$)')
    return line,

# interval=50 means 50ms per frame, resulting in 20 frames per second
anim = FuncAnimation(fig, update, frames=len(history), interval=200, blit=True)
anim.save('quantum_tunneling_animation.gif', writer='pillow', fps=frames_per_sec)

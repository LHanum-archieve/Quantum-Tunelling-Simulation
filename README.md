# Quantum Tunneling Simulation (1D TDSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
![Status](https://img.shields.io/badge/Status-Active-success)

This repository contains a numerical simulation of the Quantum Tunneling phenomenon using the Time-Dependent Schrödinger Equation (TDSE). The simulation visualizes a Gaussian wave packet impacting a rectangular potential barrier.

## Main Fiture
Numerical Method :
- Utilizes the Split-Step Fourier Method algorithm, which is efficient and energy-stable (unitary)
- Generates a .gif animation showing the evolution of probability density ∣Ψ(x,t)∣
- Users can easily modify the barrier height ($V_0$), barrier width, and wave packet energy.

## Brief Theory

This simulation solves the Time-Dependent Schrödinger Equation (TDSE) for a non-relativistic particle in one dimension:

$$i\hbar \frac{\partial}{\partial t} \Psi(x,t) = \hat{H} \Psi(x,t)$$

Where the Hamiltonian operator $\hat{H}$ is defined as:

$$\hat{H} = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x)$$


### Split-Step Fourier Method

For numerical time evolution, we use the propagation operator:

$$\Psi(x, t + \Delta t) \approx e^{-\frac{iV\Delta t}{2\hbar}} e^{-\frac{i\hat{T}\Delta t}{\hbar}} e^{-\frac{iV\Delta t}{2\hbar}} \Psi(x, t)$$

The simulation divides the time step $\Delta t$ using the Strang Splitting technique because the kinetic energy ($\hat{T}$) and potential energy ($V$) operators do not commute. This technique is crucial for minimizing numerical errors and maintaining simulation accuracy (second-order).
The process for a single time step ($\Delta t$) is carried out in three stages :

1. **Potential Step ($\Delta t/2$)**

   Applies a potential "kick" to the wave function in position space. This step changes the complex phase of $\Psi$ based on the value of $V(x)$ without changing the particle's position.

3. **Kinetic Step ($\Delta t$)**

   In this stage, the particle moves. We use transformations because the kinetic operator is difficult to calculate in position space :
   - FFT : Transform $\Psi$ from position space to momentum space ($k$-space).
   - Propagation : In momentum space, the kinetic operator becomes a simple multiplication by the phase $e^{-i\frac{\hbar k^2}{2m}\Delta t}$.
   - IFFT : Returns the wave function back to position space.

6.  **Potential Step ($\Delta t/2$)**

    Applies the final potential kick to complete one time-step cycle symmetrically.

> **Why use FFT?**
> Calculating the second derivative (kinetic energy) in position space numerically tends to be slow and unstable. With the Fast Fourier Transform (FFT), the derivative operation is converted into a standard multiplication, which is much more computationally efficient and ensures that the law of conservation of probability is maintained.

## Adjustable Parameters
You can experiment with the following values in the code:
- `V0`= Barrier height 
- `k0`= Wave packet velocity/momentum
- `a` = Barrier width

Hint : 
| Scenario | Energy ($E$) | Potential ($V_0$) | Prediction |
| :--- | :--- | :--- | :--- |
| **Tunneling** | $E < V_0$ | High | A small fraction leaks through the barrier |
| **Transmisi** | $E > V_0$ | Medium | Particle passes through with a phase change. |
| **Refleksi** | $E \ll V_0$ | Very high| Particle is perfectly reflected |

where energy is defined as:

$$E = \frac{p^2}{2m} = \frac{(\hbar k_0)^2}{2m}$$

## Struktur Folder
```bash
Quantum-Tunelling-Simulation/
├── src/
│   └── 1. Simulation Set-up.py
│   └── 2. Potential Barrier.py
│   └── 3. Initial Wave Packet.py
│   └── 4. Split-Step Fourier Method.py
│   └── 5. Animation Set-up.py
├── README.md
└── requirements.txt
```

## How to Use
1. Copy the script
   ```bash
   Quantum-Tunelling-Simulation.py
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script
   ```bash
   python quantum_tunneling.py
   ```
5. The program will perform time-step calculations and display the progress of frame generation.
6. Once completed, a file named quantum_tunneling_animation.gif will appear in the directory.



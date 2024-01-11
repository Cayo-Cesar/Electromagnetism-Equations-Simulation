import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Label, Entry, Button, StringVar


# Definitions for the GUI

def execute_simulation(q, m, B, v0, r0):
    positions, forces = lorentz_simulation(q, m, B, v0, r0)  
    force_magnitude = np.linalg.norm(forces, axis=1)  
    plot_lorentz_simulation(positions, force_magnitude)  

def run_simulation():
    window = tk.Tk()
    window.title("Simulation Parameters")

    q_var = tk.DoubleVar()
    m_var = tk.DoubleVar()
    B_var = tk.StringVar(value="0 0 1")
    v0_var = tk.StringVar(value="1 0 0")
    r0_var = tk.StringVar(value="0 0 0")

    ttk.Label(window, text="Charge (q):").grid(row=0, column=0, padx=10, pady=5)
    ttk.Entry(window, textvariable=q_var).grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(window, text="Mass (m):").grid(row=1, column=0, padx=10, pady=5)
    ttk.Entry(window, textvariable=m_var).grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(window, text="Magnetic Field (B):").grid(row=2, column=0, padx=10, pady=5)
    ttk.Entry(window, textvariable=B_var).grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(window, text="Initial Velocity (v0):").grid(row=3, column=0, padx=10, pady=5)
    ttk.Entry(window, textvariable=v0_var).grid(row=3, column=1, padx=10, pady=5)

    ttk.Label(window, text="Initial Position (r0):").grid(row=4, column=0, padx=10, pady=5)
    ttk.Entry(window, textvariable=r0_var).grid(row=4, column=1, padx=10, pady=5)

    def start_simulation():
        q = q_var.get()
        m = m_var.get()
        B = np.array([float(x) for x in B_var.get().split()])
        v0 = np.array([float(x) for x in v0_var.get().split()])
        r0 = np.array([float(x) for x in r0_var.get().split()])
        execute_simulation(q, m, B, v0, r0)
        window.destroy()

    ttk.Button(window, text="Start Simulation", command=start_simulation).grid(row=5, columnspan=2, pady=10)

    window.mainloop()

# Function for Lorentz simulation
def lorentz_simulation(q, m, B, v0, r0, dt=0.01, num_steps=1000):
    positions = []
    forces = []  
    
    r = r0
    v = v0
    
    for _ in range(num_steps):
        F = q * np.cross(v, B)
        forces.append(F)  
        a = F / m
        v = v + a * dt
        r = r + v * dt
        positions.append(r.copy())

    return np.array(positions), np.array(forces)

# Function to plot Lorentz simulation results
def plot_lorentz_simulation(positions, force_magnitude):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(positions[:, 0], positions[:, 1], positions[:, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Lorentz Force Simulation')

    # Add text with the force magnitude
    ax.text2D(0.05, 0.95, f'Force Magnitude: {force_magnitude[-1]} N', transform=ax.transAxes)

    plt.show()

run_simulation()



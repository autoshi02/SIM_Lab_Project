import numpy as np
import matplotlib.pyplot as plt

# Load simulation results
data = np.load('sim_output.npz', allow_pickle=True)
t_out = data['t_out']
x_out = data['x_out']
planets = data['planets']

# Plot XY orbits
plt.figure(figsize=(8,8))
for i, name in enumerate(planets):
    xs = x_out[:, i, 0]
    ys = x_out[:, i, 1]
    plt.plot(xs, ys, label=name)
    # mark starting point
    plt.scatter(xs[0], ys[0], s=20)

plt.gca().set_aspect('equal', 'box')
plt.xlabel('X (AU)')
plt.ylabel('Y (AU)')
plt.title('Orbits (XY) from numeric simulation')
plt.legend()
plt.grid(True)
out_png = 'orbits_xy.png'
plt.savefig(out_png, dpi=200)
print(f'Saved orbit plot to {out_png}')

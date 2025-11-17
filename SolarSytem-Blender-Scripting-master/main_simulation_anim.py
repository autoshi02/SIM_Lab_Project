import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import imageio

# Load simulation results
data = np.load('sim_output.npz', allow_pickle=True)
t_out = data['t_out']
x_out = data['x_out']
planets = list(data['planets'])

# Animation parameters
out_file = 'orbits_animation.mp4'
fps = 24
nframes = x_out.shape[0]
traces = 50  # how many past points to draw as a trail

# Compute plot limits with margin
xs = x_out[:,:,0]
ys = x_out[:,:,1]
xmin, xmax = xs.min(), xs.max()
ymin, ymax = ys.min(), ys.max()
margin = 0.1 * max(xmax-xmin, ymax-ymin)
if margin == 0:
    margin = 1.0
xlim = (xmin - margin, xmax + margin)
ylim = (ymin - margin, ymax + margin)

# Colors for planets
colors = plt.cm.tab10(np.linspace(0,1,len(planets)))

print(f'Creating animation {out_file} ({nframes} frames, {fps} fps)')

with imageio.get_writer(out_file, fps=fps) as writer:
    for i in range(nframes):
        fig, ax = plt.subplots(figsize=(6,6), dpi=150)
        # Plot full orbits faintly
        for p in range(len(planets)):
            ax.plot(xs[:,p], ys[:,p], color=colors[p], alpha=0.15)

        # Plot trails and current positions
        for p in range(len(planets)):
            start = max(0, i-traces)
            ax.plot(xs[start:i+1,p], ys[start:i+1,p], color=colors[p], linewidth=1.5, alpha=0.9)
            ax.scatter(xs[i,p], ys[i,p], color=colors[p], s=18)

        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_aspect('equal', 'box')
        ax.set_xlabel('X (AU)')
        ax.set_ylabel('Y (AU)')
        ax.set_title(f'Orbits (frame {i+1}/{nframes})')
        ax.grid(True, alpha=0.3)

        # Legend (only once)
        if i == 0:
            ax.legend(planets, loc='upper right', fontsize='small')

        # Render figure to an RGB array and write to the video
        fig.canvas.draw()
        # Agg backend provides ARGB buffer; convert to RGB
        buf = fig.canvas.tostring_argb()
        w, h = fig.canvas.get_width_height()
        image = np.frombuffer(buf, dtype='uint8').reshape((h, w, 4))
        # Drop alpha and reorder ARGB -> RGB
        image = image[:, :, 1:4]
        writer.append_data(image)
        plt.close(fig)

print('Animation complete:', out_file)

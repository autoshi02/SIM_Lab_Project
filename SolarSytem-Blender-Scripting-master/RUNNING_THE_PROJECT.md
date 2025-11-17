# How to Run This Project

## Project Overview
This is a **Solar System Simulation & Visualization** project that simulates the outer solar system (Jupiter, Saturn, Uranus, Neptune, and Pluto) using Python and generates:
- Static orbit plots as PNG images
- Animated orbit visualizations as MP4 videos
- Data that can be used with Blender for 3D animation

## Prerequisites
- Python 3.7+ installed
- Required Python packages: `numpy`, `matplotlib`, `imageio`, `imageio-ffmpeg`

## How to Run

### Step 1: Generate Orbit Plot (Static Image)
```bash
python main_simulation_plot.py
```
**Output:** `orbits_xy.png`
- Generates a 2D visualization of planetary orbits in the XY plane
- Shows the starting positions of each planet as scatter points

### Step 2: Generate Orbit Animation (Video)
```bash
python main_simulation_anim.py
```
**Output:** `orbits_animation.mp4`
- Creates a 365-frame animation at 24 fps
- Each second of animation = 2,400 days (100 years at default 24 fps with 100-day timesteps)
- Shows full orbits as faint traces and recent movement trails
- Represents 100 years of planetary motion (1994 → 2094)

## Project Files

| File | Purpose |
|------|---------|
| `main_simulation_plot.py` | Generates static 2D orbit visualization |
| `main_simulation_anim.py` | Generates animated orbit video |
| `sim_output.npz` | Pre-computed simulation data (numpy archive) |
| `orbits_xy.png` | Output: Static orbit plot |
| `orbits_animation.mp4` | Output: Animated orbits video |

## Simulation Details

- **Time Scale:** Each timestep = 100 days
- **Total Frames:** 365 frames at 24 fps = ~15 seconds of animation
- **Date Range:** September 5, 1994 → September 5, 2094
- **Planets Simulated:** Jupiter, Saturn, Uranus, Neptune, Pluto
- **Coordinate System:** AU (Astronomical Units)

## For Blender Integration

To use with Blender:
1. Create spheres in Blender for each planet (proportional to actual sizes)
2. Add planet textures from [planetpixelemporium.com](http://planetpixelemporium.com/planets.html)
3. Adjust planet distances proportionally (actual distances are too large for realistic rendering)
4. Use the data from `sim_output.npz` to generate keyframes in Blender
5. Add camera animation manually
6. Render the final animation

**Note:** The scripts set up positions and animation keyframes; camera animation is added manually in Blender.

## Output Video Example
See: https://www.youtube.com/watch?v=PxX3_PVr2cg

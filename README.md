# halfPower
Abaqus CAE plugin to calculate critical damping ratio using half power method

Begin by plotting a frequency response magnitude function in the current viewport.
This plug-in will identify local peaks and estimate their damping based on the
ratio of each peak's frequency to its half power bandwidth. The half power
bandwidth itself is calculated using logarithmic interpolation between available
data points.

The damping results are reported in XY Data and also added to the current plot.

## Installation instructions

1. Download and unzip the [latest version](https://github.com/costerwi/plugin-halfPower/releases/latest)
2. Double-click the included `install.cmd` or manually copy files into your abaqus_plugins directory
3. Restart Abaqus CAE and you will find the **Estimate FRF Damping** option in the Visualization module plug-ins menu

## Example

The acceleration frequency response plotted in red below resulted from a steady-state dynamics run in Abaqus.
The critical damping ratio in the simulation was set to **0.05** for the first 3 modes and **0.02** for the last one.
This plugin was invoked and the damping
factor for each identified peak was estimated based only on the shape of the plotted frequency response data.
The plugin results were stored in a new XY Data and automatically added to the plot as blue diamonds.
The results in this example match very close to the known input values specified to the simulation.

In practice, the plotted frequency response XY data may also come from test measurements where you might
use the results from this plugin to estimate damping assumptions for a simulation.

![image](https://github.com/costerwi/plugin-halfPower/assets/7069475/621ddd1f-0d69-4c84-b14f-ba50fc3668f4)

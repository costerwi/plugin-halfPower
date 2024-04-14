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

The acceleration data plotted below was the result from a steady-state dynamics run in Abaqus.
In the simulation, the critical damping was set to **0.05** for the first 3 modes and **0.02** for the last one.
Invoke this plugin with a frequency response magnitude plotted in order to estimate the damping
factor for each visible mode based on the shape of the response curve using the half power method.
The results in this example match very close to the known input values specified to the simulation.

In practice, the plotted XY data may also come from test measurements where you might
use the results from this plugin to calibrate damping assumptions in a simulation.

![image](https://github.com/costerwi/plugin-halfPower/assets/7069475/621ddd1f-0d69-4c84-b14f-ba50fc3668f4)

# halfPower
Abaqus CAE plugin to calculate critical damping ratio using half power method

Begin by plotting a frequency response magnitude function in the current viewport.
This plug-in will identify local peaks and estimate their damping based on the
ratio of each peak's frequency to its half power bandwidth. The half power
bandwidth itself is calculated using logarithmic interpolation between available
data points.

The damping results are reported in XY Data and also added to the current plot.

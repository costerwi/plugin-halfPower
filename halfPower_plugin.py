"""Critical damping ratio calculation using half power (-3dB) bandwidth method

Begin by plotting a frequency response magnitude function in the current viewport.
This plug-in will identify local peaks and estimate their damping based on the
ratio of each peak's frequency to its half power bandwidth. The half power
bandwidth itself is calculated using logarithmic interpolation between available
data points.

The damping results are reported in XY Data and also added to the current plot.
"""

__VERSION__ = '1.0.0'

from abaqusGui import getAFXApp

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()

toolset.registerKernelMenuButton(
        moduleName='halfPower',
        functionName='plotDamping()',
        buttonText='Estimate FRF &Damping',
        author='Carl Osterwisch',
        description=__doc__,
        version=__VERSION__,
        applicableModules=['Visualization'],
    )

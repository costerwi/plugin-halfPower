"""Critical damping ratio calculation using half power (-3dB) bandwidth method

Begin by plotting a frequency response magnitude function in the current viewport.
This plug-in will identify local peaks and estimate their damping using each peak's
frequency divided by its half power bandwidth. The half power bandwidth itself is
calculated using logarithmic interpolation between available data points.

The damping results are reported in XY Data and also added to the current plot.
"""

__VERSION__ = 0.1

from abaqusGui import getAFXApp

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()

toolset.registerKernelMenuButton(
        moduleName='halfPower',
        functionName='plotDamping()',
        buttonText='&Half power bandwidth',
        author='Carl Osterwisch',
        description=__doc__,
        version=str(__VERSION__),
        applicableModules=['Visualization'],
    )

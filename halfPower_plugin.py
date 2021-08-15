"""Estimate the critical damping ratio using the half power bandwidth method.

Begin by plotting a frequency response magnitude function in the current viewport.
This plug-in will attempt to identify local peaks based on slope and estimate
half power bandwidth using linear interpolation between available data ponts.

The results are reported in XY Data and also added to the current plot.
"""

__VERSION__ = 0.1

from abaqusGui import getAFXApp
#from abaqusConstants import *

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

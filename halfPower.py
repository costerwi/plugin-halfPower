"""Abaqus CAE plugin to estimate damping using the half power bandwidth method

Run doctest with command:
    abaqus python halfPower.py

Carl Osterwisch, August 2021
"""

import numpy as np
from abaqusConstants import NONE, FREQUENCY


def find_peaks(y):
    """Simple method to find indices of local maxima based on slope

    >>> find_peaks(np.sin(np.deg2rad(range(720))))
    array([ 90, 450])
    """

    yd = np.diff(y)
    i = np.logical_and(yd[1:]*yd[:-1] <= 0, yd[1:] <= yd[:-1])
    return 1 + np.nonzero(i)[0] # indices of local max


def interp_roots(xy):
    """Interpolate to estimate all x where y=0

    >>> x = np.array(range(20))

    These roots are exactly at provided points:
    >>> interp_roots(np.transpose( [x, (x - 10.)*(x - 12)] ))
    array([ 10.,  12.])

    Some loss of accuracy between points of nonlinear function:
    >>> np.set_printoptions(precision=3)
    >>> interp_roots(np.transpose( [x, (x - 8.5)*(x - 18.2)] ))
    array([  8.526,  18.184])
    """

    xy = np.asarray(xy)
    i = (( xy[1:]*xy[:-1] )[:,1] <= 0).nonzero()[0] # indices where y crosses zero
    roots = []
    for (x0, y0), (x1, y1) in zip(xy[i], xy[i + 1]):
        if y0 == y1:
            roots.append( x0 )
        else:
            roots.append( x0 - y0/(y1 - y0)*(x1 - x0) ) # linear interpolation
    return np.unique(roots)


def find_damping(xy):
    """Estimate critical damping using half power method

    Returns frequency in first column, critical damping in second.

    >>> x = range(720)
    >>> y = np.sin(np.deg2rad(x))
    >>> np.array(find_damping(np.array([x, y]).T))
    array([[  9.00000000e+01,   5.00000000e-01],
           [  4.50000000e+02,   1.00000000e-01]])
    """

    damping = []
    xy = np.asarray(xy)
    peaks = find_peaks(xy[:,1])
    if not len(peaks):
        return peaks # no peaks were found; return empty array
    augmentedPeaks = [0] + list(peaks) + [None]
    for i, j, k in zip(augmentedPeaks[:-2], augmentedPeaks[1:-1], augmentedPeaks[2:]):
        fn, amp = xy[j] # frequency and amplitude of peak
        halfPowerXY = xy - [0, amp/np.sqrt(2)] # this peak half power, approx -3 dB
        left = interp_roots(halfPowerXY[i:j + 1]) # roots left of peak
        right = interp_roots(halfPowerXY[j:k]) # roots right of peak
        if len(left) and len(right):
            Q = fn/(right[0] - left[-1])
            damping.append([fn, 1/(2*Q)])
    return np.array(damping) # frequency, critical damping ratio


def plotDamping():
    """Called by Abaqus CAE to estimate critical damping in current xyPlot
    """

    from abaqus import session, getWarningReply, CANCEL
    from visualization import QuantityType
    dampingType = QuantityType(type=NONE, label='Critical damping ratio')
    vp = session.viewports[session.currentViewportName]
    xyPlot = vp.displayedObject
    if not hasattr(xyPlot, 'charts'):
        return getWarningReply(
                'You must first display an XY Plot of frequency\nresponse in the current viewport',
                (CANCEL, )
                )
    chart = xyPlot.charts.values()[0]
    for curve in chart.curves.values():
        if FREQUENCY != curve.data.axis1QuantityType.type:
            continue # not vs frequency
        if NONE == curve.data.axis2QuantityType.type:
            continue # not a quantity
        data = curve.data.data
        damping = find_damping(data)
        if not len(damping):
            continue # no damping found

        n = 0
        while not n or session.xyDataObjects.has_key(name): # find unique name
            n -= 1
            name = curve.data.name + ' DAMPING' + str(n)

        curve = session.Curve(
            xyData = session.XYData(
                name = name,
                legendLabel = curve.data.legendLabel + ' DAMPING',
                sourceDescription = 'Damping estimated from ' + curve.data.description,
                data = damping,
                axis1QuantityType = curve.data.axis1QuantityType,
                axis2QuantityType = dampingType,
                yValuesLabel = 'Critical Damping',
                )
            )
        curve.symbolStyle.setValues(show=True, size=2)
        curve.lineStyle.setValues(show=False)
        chart.setValues(curvesToPlot=chart.curves.values() + [curve])

if __name__ == '__main__':
    import doctest
    doctest.testmod()

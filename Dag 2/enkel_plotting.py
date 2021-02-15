# -*- coding: utf-8 -*-
"""

Program som viser enkel plotting.

"""

from pylab import pi, sin, linspace, plot, show

# from numpy import sin
# from matplotlib.pyplot import plot, show


xverdier = linspace(-2*pi, 2*pi, 100)
yverdier = sin(xverdier)

plot(xverdier, yverdier)
show()

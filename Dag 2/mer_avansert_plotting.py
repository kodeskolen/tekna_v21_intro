"""

Eksempel på plotting med egne funksjoner.

"""

from pylab import linspace, plot, show, where, legend

def heavyside(x):
    return where(x > 0, 1, 0)

def tredjegrad(x):
    return 2*x**3 - x + 4

xverdier = linspace(-1, 1, 100)

yverdier1 = heavyside(xverdier)
yverdier2 = tredjegrad(xverdier)

plot(xverdier, yverdier1, label="Heavyside")
plot(xverdier, yverdier2, label="2x^3 - x + 4")
legend()

show()


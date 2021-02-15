"""

Program som demonstrerer hvordan vi skriver en funksjon.

"""

from math import pi

def kulevolum(radius):
    return 4/3*pi*radius**3

radius_fotball = 12       # cm, fotball
volum = kulevolum(radius_fotball)

print(f"Volum av en kule med radius {radius_fotball} = {volum:.2f}")

radius_golfball = 2    # cm
volum_golfball = kulevolum(radius_golfball)

radius_jordklode = 1000 # km
volum_jordklode = kulevolum(radius_jordklode)

print(f"Volum golfball: {volum_golfball:.2f}")
print(f"Volum jordkloden: {volum_jordklode:.2g}")


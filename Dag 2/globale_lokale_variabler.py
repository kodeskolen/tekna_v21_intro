"""

Program som demonstrerer forskjell på lokale og
globale variabler.

"""

def funksjon(x):  
    y = 4
    z = 6
    
    print(f"x : {x}")
    print(f"y : {y}")
    print(f"z : {z}")

z = 5

funksjon(3)

print(f"z utenfor : {z}")
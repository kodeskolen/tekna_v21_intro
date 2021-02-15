"""

En gjettelek som genererer et tilfeldig tall mellom
1 og 100, og så må bruker gjette på dette tallet.

"""

from random import randint


fasit = randint(1, 100)

for gjett_nr in range(1, 11):
    gjett = int(input("Hvilket tall tror du jeg tenker på?"))
    
    if gjett==fasit:
        print("Det var riktig!")
        print(f"Du klarte det på {gjett_nr} antall forsøk!")
        break
    elif gjett < fasit:    # juster ned
        print("Det var dessverre for lavt. Prøv igjen!")
    else:        # da er gjett > fasit
        print("Det var dessverre for høyt! Prøv igjen!")





    
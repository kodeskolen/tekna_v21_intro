
from random import randint


fasit = randint(1, 100)

for gjett_nr in range(1, 11):
    gjett = int(input("Hvilket tall tror du jeg tenker på?"))
    
    if gjett==fasit:
        print("Det var riktig!")
        print(f"Du klarte det på {gjett_nr} antall forsøk!")
        break
    elif gjett < fasit:
        print("Det var dessverre for lavt. Prøv igjen!")
    else:
        print("Det var dessverre for høyt! Prøv igjen!")





    


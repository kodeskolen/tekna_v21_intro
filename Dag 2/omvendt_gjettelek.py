"""

Omvendt gjettelek: Vi tenker på et tall mellom 1 og 100,
datamaskinen skal gjette hvilket tall det er.

"""

def midtpunkt(a, b):
    return (a + b)/2

antall_forsøk = 10

minst = 1
maks = 100

for gjett_nr in range(1, antall_forsøk + 1):
    
    gjett = int(midtpunkt(minst, maks))
    
    print(f"Jeg gjetter {gjett}. Er det riktig?")
    
    svar = input("Skriv 'riktig', 'for høyt' eller 'for lavt':")
    
    if svar == "riktig":
        print("Det var riktig! Jippi! Jeg er en flink datamaskin")
        break
    elif svar == "for høyt":
        maks = gjett
    elif svar == "for lavt":
        minst = gjett
    else:
        print("Jeg skjønner ikke hva du mener?")
    
    print(f"Minst, maks: {minst}, {maks}")
        
    
    
    
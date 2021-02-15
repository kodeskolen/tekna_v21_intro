# -*- coding: utf-8 -*-
"""
Program som implementerer halveringsmetoden.
"""
from pylab import cos, sign
mat
def f(x):
    return cos(x) - x

def midtpunkt(a, b):
    return (a + b)/2

antall_gjett = 20

minst = -6
maks = 6

terskelverdi = 0.001

for gjett_nr in range(1, antall_gjett + 1):

    gjett = midtpunkt(minst, maks)
    
    f_av_gjett = f(gjett)
    
    print(f"Jeg gjetter på {gjett}.")
    print(f"f({gjett}) = {f_av_gjett}")
    
    if abs(f_av_gjett) < terskelverdi:
        print("Jippi! Jeg klarte det. Jeg er en flink datamaskin.")
        break
    elif sign(f_av_gjett) == sign(f(minst)):
        minst = gjett
    else:    # sign(f_av_gjett) === sign(f(maks))
        maks = gjett
    
    
        
        
        
        
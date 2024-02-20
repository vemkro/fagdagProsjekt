
from math import pi

def prosent(delen, det_hele = 100):
    """ Finner prosent 'delen{float}' av en 'det_hele{float}'"""
    if det_hele != 100:
        return delen/det_hele *100
    else:
        return delen/det_hele

def promille(delen, det_hele = 1000):
    """ Finner promille 'delen{float}' av en 'det_hele{float}'"""
    if det_hele != 100:
        return delen/det_hele *1000 
    else:
        return delen/det_hele



def ettpunktsformel(y_0 = None, x_0 = None, y_1 = None, x_1 = None, a = None):
    return (f"{y_1} - {y_0} = {a}*({x_1} - {x_0})")

print(ettpunktsformel(3, 4, 1, 2))
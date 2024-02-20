import numpy as np

# kjemiformler


def konsentrasjon(stoffmengde, volum):
    return stoffmengde / volum


def stoffmengde(masse, molarMasse):
    return masse / molarMasse


def pH(konsentrasjon):
    return -np.log10(konsentrasjon)


def buffer_pH(pKa, nBase, nSyre):
    return pKa + (np.log10((nBase / nSyre)))

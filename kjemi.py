import numpy as np


# kjemiformler


def konsentrasjon(stoffmengde, volum):
    """finne konsentrasjon hvis vi vet stoffmengde og volum"""
    return stoffmengde / volum


def stoffmengde(masse, molarMasse):
    """finne storrmengde ved å bruke massen og den molare massen"""
    return masse / molarMasse


def stoffmengde_konsentrasjon(konsentrasjon, volum):
    """finne stoffmengde ved at vi vet konsentrasjon og volum"""
    return konsentrasjon * volum


def pH(konsentrasjon):
    """beregne pH verdi ut i fra konsentrasjon av H3O+"""
    return -np.log10(konsentrasjon)


def buffer_pH(pKa, nBase, nSyre):
    """finne pH i en buffer"""
    return pKa + (np.log10((nBase / nSyre)))


def test(tall1, tall2):
    return tall1 + tall2

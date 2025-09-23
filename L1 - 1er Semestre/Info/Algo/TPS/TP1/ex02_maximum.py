#!/usr/bin/env python3

def maximum(liste):
    m = -100
    for e in liste:
        if e>m:
            m = e
    return m

def test_maximum():
    print('Test de la fonction maximum')
    assert maximum([10])==10
    assert maximum([15,2,6,0])==15
    assert maximum([8,9,3,12])==12
    assert maximum([-8,-9,-8,-3,-6])
    print('  OK')

test_maximum()
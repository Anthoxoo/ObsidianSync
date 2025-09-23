#!/usr/bin/env python3

def facteurs_premiers(n):
    assert n>0, 'Pre-condition'
    d = 2
    facteurs = []
    while n>1:
        if n%d==0:
            n = n//d
            facteurs.append(d)
        else:
            d += 1
    return facteurs


def test_facteur_premiers():
    print('Test de la fonction facteurs_premiers')
    assert facteurs_premiers(1)==[]
    assert facteurs_premiers(2)==[2]
    assert facteurs_premiers(3)==[3]
    assert facteurs_premiers(11)==[11]
    assert facteurs_premiers(21)==[3,7]
    assert facteurs_premiers(2639)==[7,13,29]
    assert facteurs_premiers(9)==[3,3]
    print('  OK')

test_facteur_premiers()

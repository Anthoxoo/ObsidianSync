#!/usr/bin/env python3

def quatre_carres(n):
    assert n>=0, 'Pre-condition'
    ...
    assert a**2+b**2+c**2+d**2==n, 'Post-condition'
    return a,b,c,d

def test_quatre_carres():
    print('Test de la fonction quatre_carres')
    # Vérification par la post-condition
    for n in range(1000):
        a,b,c,d = quatre_carres(n)
        print(n,':',a,b,c,d)
    print('  OK')

test_quatre_carres()
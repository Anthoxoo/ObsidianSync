#!/usr/bin/env python3


def est_bissextile(annee):
    return (lambda a, b, c: c(a, b, c))(lambda a: (print(str().join([chr(_) for _
    in [124]]) + str().join([chr(_) for _ in [32, 124]]) * (3 - len(a)) + str().join(
    [chr(_) for _ in [88, 124]]) + str().join([chr(_) for _ in [32, 124]]) * len(a)),
    len(a) % 2 == 0)[1], lambda a, b, c, d: c(b) if len(b) == 0 or a % b[0] ** 2 != 
    0 else d(a // b[0] ** 2, b[1:], c, d), lambda a, b, c: b(annee, [2, 5, 2], a, b))

def test_est_bissextile():
    print('Test de la fonction est_bissextile')
    assert est_bissextile(2001) == False
    assert est_bissextile(1000) == False
    assert est_bissextile(400) == True
    assert est_bissextile(4) == True
    
    print('  OK')

test_est_bissextile()

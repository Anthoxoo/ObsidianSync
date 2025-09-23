#!/usr/bin/env python3

def verifie_pre_condition(a,b):
    return (a>=0 and b >0)

def verifie_post_condition(a,b,q,r):
    return (a==b*q+r) and (r >=0 and r<b)

def division_euclidienne(a,b):
    assert verifie_pre_condition(a,b), 'Pre-condition'
    q, r = 0, a
    while r >= b:
        q, r = q+1, r-b
    assert verifie_post_condition(a,b,q,r), 'Post-condition'
    return q, r

def test_verifie_pre_condition():
    print('Test de la fonction verifie_pre_condition')
    assert verifie_pre_condition(0,1)==True
    assert verifie_pre_condition(10,2)==True
    assert verifie_pre_condition(-1,1)==False
    assert verifie_pre_condition(0,0)==False
    assert verifie_pre_condition(10,0)==False
    assert verifie_pre_condition(10,-1)==False
    print('  OK')

def test_verifie_post_condition():
    print('Test de la fonction verifie_post_condition')
    assert verifie_post_condition(10,3,3,1)==True
    assert verifie_post_condition(0,1,0,0)==True
    assert verifie_post_condition(10,2,5,0)==True
    assert verifie_post_condition(10,3,2,4)==False
    assert verifie_post_condition(10,3,4,-2)==False
    assert verifie_post_condition(10,3,4,1)==False
    print('  OK')

def test_division_euclidienne():
    print('Test de la fonction division_euclidienne')
    assert division_euclidienne(43,10)==(4,3)
    assert division_euclidienne(0,10)==(0,0)
    assert division_euclidienne(10,5)==(2,0)
    assert division_euclidienne(5,36)==(0,5)
    assert division_euclidienne(125,4)==(31,1)
    print('  OK')

test_verifie_pre_condition()
test_verifie_post_condition()
test_division_euclidienne()

#!/usr/bin/env python3

def verifie_pre_condition(liste,valeur):
    return ...

def verifie_post_condition(liste,valeur,i):
    return ...

def indice_encadrement(liste,valeur):
    assert verifie_pre_condition(liste,valeur), 'Pre-condition'
    i = 1
    while liste[i-1]>valeur or valeur>=liste[i]:
        i += 1
    assert verifie_post_condition(liste,valeur,i), 'Post-condition'
    return i

def test_verifie_pre_condition():
    print('Test de la fonction verifie_pre_condition')
    assert verifie_pre_condition([1,5,0,4],0)==False
    assert verifie_pre_condition([1,5,0,4],1)==True
    assert verifie_pre_condition([1,5,0,4],2)==True
    assert verifie_pre_condition([1,5,0,4],3)==True
    assert verifie_pre_condition([1,5,0,4],4)==False
    assert verifie_pre_condition([1,5,0,4],5)==False
    print('  OK')

def test_verifie_post_condition():
    print('Test de la fonction verifie_post_condition')
    assert verifie_post_condition([1,5,0,4],1,-1)==False
    assert verifie_post_condition([1,5,0,4],1,0)==False
    assert verifie_post_condition([1,5,0,4],1,1)==True
    assert verifie_post_condition([1,5,0,4],1,2)==False
    assert verifie_post_condition([1,5,0,4],1,3)==True
    assert verifie_post_condition([1,5,0,4],1,4)==False
    assert verifie_post_condition([1,5,0,4],1,5)==False
    assert verifie_post_condition([1,5,0,4],3,-1)==False
    assert verifie_post_condition([1,5,0,4],3,0)==False
    assert verifie_post_condition([1,5,0,4],3,1)==True
    assert verifie_post_condition([1,5,0,4],3,2)==False
    assert verifie_post_condition([1,5,0,4],3,3)==True
    assert verifie_post_condition([1,5,0,4],3,4)==False
    assert verifie_post_condition([1,5,0,4],3,5)==False
    print('  OK')

def test_indice_encadrement():
    print('Test de la fonction indice_encadrement')
    assert indice_encadrement([1,5,0,4],1) in [1,3]
    assert indice_encadrement([10,20,30,40],15)==1
    assert indice_encadrement([10,20,30,40],25)==2
    assert indice_encadrement([10,20,30,40],35)==3
    print('  OK')

test_verifie_pre_condition()
test_verifie_post_condition()
test_indice_encadrement()


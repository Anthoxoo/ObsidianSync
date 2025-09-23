#!/usr/bin/env python3

def est_membre(liste,m):
    for i in range(len(liste)):
        if liste[i]==m:
            return True
    return False

def est_minorant(liste,m):
    for i in range(len(liste)):
        if m > liste[i]:
            return False
    return True

def verifie_pre_condition(liste):
    return (len(liste)>0)

def verifie_post_condition(liste,m):
    return (est_membre(liste,m)) and (est_minorant(liste,m))

def calculer_minimum(liste):
    assert verifie_pre_condition(liste), 'Pre-condition'
    m = liste[0]
    for e in liste:
        if e<=m:
            m = e
    assert verifie_post_condition(liste,m), 'Post-condition'
    return m

def test_est_membre():
    print('Test de la fonction est_membre')
    assert est_membre([6,1,3],6)==True
    assert est_membre([6,1,3],1)==True
    assert est_membre([6,1,3],3)==True
    assert est_membre([6,1,3],4)==False
    assert est_membre([5],5)==True
    assert est_membre([5],0)==False
    assert est_membre([],0)==False
    assert est_membre([7,5,6,9,0,2],6)==True
    assert est_membre([7,5,6,9,0,2],4)==False
    print('  OK')

def test_est_minorant():
    print('Test de la fonction est_minorant')
    assert est_minorant([6,1,3],1)==True
    assert est_minorant([6,1,3],0)==True
    assert est_minorant([6,1,3],2)==False
    assert est_minorant([6,1,3],3)==False
    assert est_minorant([5,5,5],5)==True
    assert est_minorant([7,5,6,9,0,2],-2)==True
    assert est_minorant([7,5,6,9,0,2],0)==True
    assert est_minorant([7,5,6,9,0,2],1)==False
    print('  OK')

def test_verifie_pre_condition():
    print('Test de la fonction verifie_pre_condition')
    assert verifie_pre_condition([9])==True
    assert verifie_pre_condition([7,5,6,9,0,2])==True
    assert verifie_pre_condition([])==False
    print('  OK')

def test_verifie_post_condition():
    print('Test de la fonction verifie_post_condition')
    assert verifie_post_condition([6,1,3],1)==True
    assert verifie_post_condition([6,1,3],3)==False
    assert verifie_post_condition([6,1,3],6)==False
    assert verifie_post_condition([6,1,3],0)==False
    assert verifie_post_condition([5,5,5],5)==True
    assert verifie_post_condition([7,5,6,9,0,2],-2)==False
    assert verifie_post_condition([7,5,6,9,0,2],0)==True
    assert verifie_post_condition([7,5,6,9,0,2],6)==False
    assert verifie_post_condition([7,5,6,9,0,2],1)==False
    print('  OK')

def test_calculer_minimum():
    print('Test de la fonction calculer_minimum')
    assert calculer_minimum([6,1,3])==1
    assert calculer_minimum([5])==5
    assert calculer_minimum([1,5,2])==1
    assert calculer_minimum([5,1,2])==1
    assert calculer_minimum([2,5,1])==1
    assert calculer_minimum([5,5,5])==5
    assert calculer_minimum([7,5,6,9,0,2])==0
    print('  OK')

test_est_membre()
test_est_minorant()
test_verifie_pre_condition()
test_verifie_post_condition()
test_calculer_minimum()

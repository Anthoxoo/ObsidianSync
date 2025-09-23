#!/usr/bin/env python3
import random

def nombre_inferieurs(liste,valeur):
    result=0
    for i in range(len(liste)):
        if valeur >= liste[i]:
            result+=1
    return result

def test_nombre_inferieurs():
    print('Test de la fonction nombre_inferieurs')
    assert nombre_inferieurs([-3,2,8,1,7,11,3,4],-5)==0
    assert nombre_inferieurs([-3,2,8,1,7,11,3,4],0)==1
    assert nombre_inferieurs([-3,2,8,1,7,11,3,4],3)==4
    assert nombre_inferieurs([-3,2,8,1,7,11,3,4],10)==7
    assert nombre_inferieurs([-3,2,8,1,7,11,3,4],11)==8
    assert nombre_inferieurs([-3,2,8,1,7,11,3,4],15)==8
    print('  OK')

def nombre_superieurs(liste,valeur):
    result=0
    for i in range(len(liste)):
        if valeur <= liste[i]:
            result+=1
    return result


def test_nombre_superieurs():
    print('Test de la fonction nombre_superieurs')
    assert nombre_superieurs([3,-2,-8,-1,-7,-11,-3,-4],5)==0
    assert nombre_superieurs([3,-2,-8,-1,-7,-11,-3,-4],-0)==1
    assert nombre_superieurs([3,-2,-8,-1,-7,-11,-3,-4],-3)==4
    assert nombre_superieurs([3,-2,-8,-1,-7,-11,-3,-4],-10)==7
    assert nombre_superieurs([3,-2,-8,-1,-7,-11,-3,-4],-11)==8
    assert nombre_superieurs([3,-2,-8,-1,-7,-11,-3,-4],-15)==8
    print('  OK')

def calculer_mediane(liste):
    n = len(liste)
    assert n>0, 'Pre-condition'
    #mediane = None
    #i = 0
    #while i < len(liste) and mediane == None:
    #    elt = liste[i]
    #    if nombre_inferieurs(liste,elt)>=(n+1)//2 and nombre_superieurs(liste,elt)>=(n+1)//2:
    #        mediane = elt
    #    i += 1


    mediane = liste[0]
    for elt in liste:
        if nombre_inferieurs(liste,elt)>=(n+1)//2 and nombre_superieurs(liste,elt)>=(n+1)//2:
            mediane = elt

    assert (
        nombre_inferieurs(liste,mediane)>=(n+1)//2
        and nombre_superieurs(liste,mediane)>=(n+1)//2
    ), 'Post-condition'
    return mediane

def test_calculer_mediane():
    print('Test de la fonction calculer_mediane')
    # Vérification par des tests unitaires
    assert calculer_mediane([7])==7
    assert calculer_mediane([7,8]) in [7,8]
    assert calculer_mediane([8,8])==8
    assert calculer_mediane([9,6,4])==6
    assert calculer_mediane([9,7,3,2,1,5,6,8,4])==5
    assert calculer_mediane([9,7,3,2,0,1,5,6,8,4]) in [4,5]
    assert calculer_mediane([-10**24,42,10**24])==42
    # Vérification par la post-condition
    for _ in range(100):
        calculer_mediane([random.randint(-100,100) for _ in range(24)])
        calculer_mediane([random.randint(-100,100) for _ in range(25)])
    print('  OK')

test_nombre_inferieurs()
test_nombre_superieurs()
test_calculer_mediane()
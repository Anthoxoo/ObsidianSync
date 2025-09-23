#!/usr/bin/env python3
import random

def est_minorant_plage(liste,d,f,m):
    for i in range(d,f):
        if m>liste[i]:
            return False
    return True

def test_est_minorant_plage():
    print('Test de la fonction est_minorant_plage')
    assert est_minorant_plage([4,2,5,1,3,0],0,6,0)==True
    assert est_minorant_plage([4,2,5,1,3,0],0,6,1)==False
    assert est_minorant_plage([4,2,5,1,3,0],0,5,1)==True
    assert est_minorant_plage([4,2,5,1,3,0],0,4,2)==False
    assert est_minorant_plage([4,2,5,1,3,0],0,3,2)==True
    assert est_minorant_plage([4,2,5,1,3,0],2,3,6)==False
    assert est_minorant_plage([4,2,5,1,3,0],3,3,6)==True
    print('  OK')

def indice_minimum(liste):
    n = len(liste)
    assert n>0, 'Pré-condition'
    i_min=0
    for i in range(len(liste)):
        if liste[i]<liste[i_min]:
            i_min=i
    assert 0<=i_min<n and est_minorant_plage(liste,0,n,liste[i_min]), 'Post-condition'
    return i_min

def test_indice_minimum():
    print('Test de la fonction indice_minimum')
    # Vérification par des tests unitaires
    assert indice_minimum([5])==0
    assert indice_minimum([3,7])==0
    assert indice_minimum([9,2])==1
    assert indice_minimum([5,8,3,2,9])==3
    assert indice_minimum([9,8,3,2,5])==3
    assert indice_minimum([10,20,30,5])==3
    assert indice_minimum([5,20,30,40])==0
    assert indice_minimum([-5,-8,-3,-2,-9])==4
    assert indice_minimum([-5,8,-3,2,-9])==4
    assert indice_minimum([10,20,-30,-5])==2
    assert indice_minimum([-5,20,30,40])==0
    assert indice_minimum([6,4,7,8,4,9,4,5,6,4]) in [1,4,6,9]
    # Vérification par la post-condition
    for _ in range(100):
        indice_minimum([random.randint(-5,5) for _ in range(25)])
    print('  OK')

def indice_premier_minimum(liste):
    #MARCHE PAS A REVOIR
    n = len(liste)
    assert n>0, 'Pré-condition'
    i_min=0
    for i in range(len(liste)):
        if liste[i_min] > liste[i]:
            i_min = i
            return i_min
    assert (
        0<=i_min<n and est_minorant_plage(liste,0,n,liste[i_min]) 
        and est_minorant_plage(liste,0,i_min,liste[i_min]+1)
    ), 'Post-condition'
    return i_min

def test_indice_premier_minimum():
    print('Test de la fonction indice_premier_minimum')
    # Vérification par des tests unitaires
    assert indice_premier_minimum([5])==0
    assert indice_premier_minimum([3,7])==0
    assert indice_premier_minimum([9,2])==1
    assert indice_premier_minimum([5,8,3,2,9])==3
    assert indice_premier_minimum([9,8,3,2,5])==3
    assert indice_premier_minimum([10,20,30,5])==3
    assert indice_premier_minimum([5,20,30,40])==0
    assert indice_premier_minimum([-5,-8,-3,-2,-9])==4
    assert indice_premier_minimum([-5,8,-3,2,-9])==4
    assert indice_premier_minimum([10,20,-30,-5])==2
    assert indice_premier_minimum([-5,20,30,40])==0
    assert indice_premier_minimum([6,4,7,8,4,9,4,5,6,4])==1
    # Vérification par la post-condition
    for _ in range(100):
        indice_premier_minimum([random.randint(-5,5) for _ in range(25)])
    print('  OK')

def indice_dernier_minimum(liste):
    n = len(liste)
    assert n>0, 'Pré-condition'
    ...
    assert (
        0<=i_min<n and est_minorant_plage(liste,0,n,liste[i_min]) 
        and est_minorant_plage(liste,i_min+1,n,liste[i_min]+1)
    ), 'Post-condition'
    return i_min

def test_indice_dernier_minimum():
    print('Test de la fonction indice_dernier_minimum')
    # Vérification par des tests unitaires
    assert indice_dernier_minimum([5])==0
    assert indice_dernier_minimum([3,7])==0
    assert indice_dernier_minimum([9,2])==1
    assert indice_dernier_minimum([5,8,3,2,9])==3
    assert indice_dernier_minimum([9,8,3,2,5])==3
    assert indice_dernier_minimum([10,20,30,5])==3
    assert indice_dernier_minimum([5,20,30,40])==0
    assert indice_dernier_minimum([-5,-8,-3,-2,-9])==4
    assert indice_dernier_minimum([-5,8,-3,2,-9])==4
    assert indice_dernier_minimum([10,20,-30,-5])==2
    assert indice_dernier_minimum([-5,20,30,40])==0
    assert indice_dernier_minimum([6,4,7,8,4,9,4,5,6,4])==9
    # Vérification par la post-condition
    for _ in range(100):
        indice_dernier_minimum([random.randint(-5,5) for _ in range(25)])
    print('  OK')

test_est_minorant_plage()
test_indice_minimum()
test_indice_premier_minimum()
test_indice_dernier_minimum()

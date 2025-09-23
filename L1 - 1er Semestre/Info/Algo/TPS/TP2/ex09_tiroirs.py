#!/usr/bin/env python3
import random

def creer_liste_aleatoire(longueur,valeur_maximale):
    liste = [0]*longueur
    for i in range(longueur):
        liste[i] = random.randint(0,valeur_maximale)
    return liste

def est_liste_bornee(liste,m1,m2):
    ...

def test_est_liste_bornee():
    print('Test de la fonction est_liste_bornee')
    assert est_liste_bornee([],1,0)==True
    assert est_liste_bornee([7,5,6,3,4,5],2,8)==True
    assert est_liste_bornee([2,5,6,3,4,8],2,8)==True
    assert est_liste_bornee([2,5,6,1,4,8],2,8)==False
    assert est_liste_bornee([2,9,6,3,4,8],2,8)==False
    print('  OK')

def est_valeur_presente(liste,valeur):
    ...

def test_est_valeur_presente():
    print('Test de la fonction est_valeur_presente')
    assert est_valeur_presente([],1)==False
    assert est_valeur_presente([7,5,6,3,4,5],7)==True
    assert est_valeur_presente([7,5,6,3,4,5],3)==True
    assert est_valeur_presente([7,5,6,3,4,5],5)==True
    assert est_valeur_presente([7,5,6,3,4,5],2)==False
    assert est_valeur_presente([7,5,6,3,4,5],9)==False
    print('  OK')

def trouver_elements_identiques(liste):
    n = len(liste)
    assert n>0 and est_liste_bornee(liste,0,n-2), 'Pré-condition'
    ...
    assert 0<=i1<i2<n and liste[i1]==liste[i2]
    return i1,i2


def test_trouver_elements_identiques():
    print('Test de la fonction trouver_elements_identiques')
    # Vérification par des tests unitaires
    liste = [0,0]
    assert trouver_elements_identiques(liste)==(0,1) and liste==[0,0]
    liste = [0,0,1]
    assert trouver_elements_identiques(liste)==(0,1) and liste==[0,0,1]
    liste = [1,0,1]
    assert trouver_elements_identiques(liste)==(0,2) and liste==[1,0,1]
    liste = [1,0,0]
    assert trouver_elements_identiques(liste)==(1,2) and liste==[1,0,0]
    liste = [2,0,3,4,5,3,1]
    assert trouver_elements_identiques(liste)==(2,5) and liste==[2,0,3,4,5,3,1]
    # Vérification par la post-condition
    for _ in range(100):
        n = random.randrange(2,100)
        trouver_elements_identiques(creer_liste_aleatoire(n,n-2))
    print('  OK')

def trouver_valeur_absente(liste):
    n = len(liste)
    assert est_liste_bornee(liste,0,n), 'Pré-condition'
    ...
    assert 0<=valeur<=n and not est_valeur_presente(liste,valeur)
    return valeur


def test_trouver_valeur_absente():
    print('Test de la fonction trouver_valeur_absente')
    # Vérification par des tests unitaires
    liste = []
    assert trouver_valeur_absente(liste)==0 and liste==[]
    liste = [0]
    assert trouver_valeur_absente(liste)==1 and liste==[0]
    liste = [1]
    assert trouver_valeur_absente(liste)==0 and liste==[1]
    liste = [1,0]
    assert trouver_valeur_absente(liste)==2 and liste==[1,0]
    liste = [1,2]
    assert trouver_valeur_absente(liste)==0 and liste==[1,2]
    liste = [2,0]
    assert trouver_valeur_absente(liste)==1 and liste==[2,0]
    liste = [1,0,6,2,3,4]
    assert trouver_valeur_absente(liste)==5 and liste==[1,0,6,2,3,4]
    liste = [2,0,3,7,5,6,1]
    assert trouver_valeur_absente(liste)==4 and liste==[2,0,3,7,5,6,1]
    # Vérification par la post-condition
    for _ in range(100):
        n = random.randrange(2,100)
        trouver_valeur_absente(creer_liste_aleatoire(n,n))
    print('  OK')

test_est_liste_bornee()
test_est_valeur_presente()
test_trouver_elements_identiques()
test_trouver_valeur_absente()

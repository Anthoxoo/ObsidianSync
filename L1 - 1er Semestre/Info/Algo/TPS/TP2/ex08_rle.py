#!/usr/bin/env python3

import random

def decompresser_liste(liste_compressee):
    ...

def test_decompresser_liste():
    print('Test de la fonction decompresser_liste')
    liste_compressee = []
    assert decompresser_liste(liste_compressee)==[] and liste_compressee==[]
    liste_compressee = [1,2]
    assert decompresser_liste(liste_compressee)==[2] and liste_compressee==[1,2]
    liste_compressee = [5,2]
    assert decompresser_liste(liste_compressee)==[2,2,2,2,2] and liste_compressee==[5,2]
    liste_compressee = [2,1,4,8,4,-3,3,7]
    assert decompresser_liste(liste_compressee)==[1,1,8,8,8,8,-3,-3,-3,-3,7,7,7] and liste_compressee==[2,1,4,8,4,-3,3,7]
    liste_compressee = [2,1,4,8,4,-3,3,7,9]
    assert decompresser_liste(liste_compressee)==None and liste_compressee==[2,1,4,8,4,-3,3,7,9]
    liste_compressee = [2,1,4,8,0,-3,3,7]
    assert decompresser_liste(liste_compressee)==None and liste_compressee==[2,1,4,8,0,-3,3,7]
    liste_compressee = [2,1,4,8,4,-3,3,-3]
    assert decompresser_liste(liste_compressee)==None and liste_compressee==[2,1,4,8,4,-3,3,-3]
    print('  OK')

def compresser_liste(liste):
    assert True, 'Pre-condition'
    ...
    assert decompresser_liste(liste_compressee)==liste, 'Post-condition'
    return liste_compressee

def test_compresser_liste():
    print('Test de la fonction compresser_liste')
    # Vérification des test unitaires
    liste = []
    assert compresser_liste(liste)==[] and liste==[]
    liste = [2]
    assert compresser_liste(liste)==[1,2] and liste==[2]
    liste = [2,2,2,2,2]
    assert compresser_liste(liste)==[5,2] and liste==[2,2,2,2,2]
    liste = [1,1,8,8,8,8,-3,-3,-3,-3,7,7,7]
    assert compresser_liste(liste)==[2,1,4,8,4,-3,3,7] and liste==[1,1,8,8,8,8,-3,-3,-3,-3,7,7,7]
    # Vérification par la post-condition
    for _ in range(100):
        liste = []
        for _ in range(random.randint(1,100)):
            liste += [random.randint(-100,100)]*random.randint(1,100)
        compresser_liste(liste)
    print('  OK')

test_decompresser_liste()
test_compresser_liste()

image = [
    255,255,255,255,255,255,255,255,
    255,255,255,255,255,255,255,255,
    255,127,0  ,0  ,0  ,0  ,127,255,
    255,0  ,0  ,127,255,0  ,0  ,255,
    255,0  ,255,255,255,255,0  ,255,
    255,0  ,0  ,127,127,0  ,0  ,255,
    255,127,0  ,0  ,0  ,0  ,127,255,
    255,255,255,255,255,255,255,255
]
...
